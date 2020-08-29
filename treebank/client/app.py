import os

from copy import deepcopy
from datetime import timezone

from flask import Flask, render_template, request, url_for

from database import db


app = Flask(__name__)

audio_dir = 'static/audio'
os.makedirs(audio_dir, exist_ok=True)

tree_dir = 'static/tree'
os.makedirs(tree_dir, exist_ok=True)

PAGE_SIZE = 10


@app.route('/')
@app.route('/index')
def main():
    page = request.args.get('page', 1, type=int)

    query = db.texts.find().sort('created', -1)
    raw_texts = query.skip((page - 1) * PAGE_SIZE).limit(PAGE_SIZE)

    pagination = {
        'page': page,
        'prev_url': None if page == 1 else url_for('main', page=page-1),
        'next_url': None if query.count() <= (page * PAGE_SIZE)
        else url_for('main', page=page+1)
    }

    texts = list()
    for text in raw_texts:
        formatted = deepcopy(text)

        identifier = text['_id']
        audio_file = f'{tree_dir}/{identifier}.wav'
        if identifier not in os.listdir(tree_dir):
            with open(audio_file, 'wb') as audio_bin:
                audio_bin.write(text['audio_bin'])
        formatted['audio'] = audio_file

        text['created'].replace(tzinfo=timezone.utc)
        formatted['created'] = text['created'].strftime(
            '%B %d, %Y %I:%M:%S %p %z')

        formatted['pos_tagged'] = ', '.join(
            f'{word} - {tag}' for word, tag in text['pos_tagged'])

        formatted['named_entities'] = ', '.join(
            f'{word} - {entity}' for word, entity in text['named_entities'])

        formatted['productions'] = ', '.join(
            f'{lhs} -> {" ".join(r for r in rhs)} [{prob}]'
            for lhs, rhs, prob in text['productions'])

        formatted['pcfg'] = f'{text["pcfg"]:.2e}'

        tree_file = f'{tree_dir}/{identifier}.png'
        if identifier not in os.listdir(tree_dir):
            with open(tree_file, 'wb') as tree_bin:
                tree_bin.write(text['tree_bin'])
        formatted['tree'] = tree_file

        texts.append(formatted)

    return render_template('data.html', texts=texts, pagination=pagination)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
