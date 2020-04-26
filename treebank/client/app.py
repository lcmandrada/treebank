import os

from copy import deepcopy
from datetime import timezone

from flask import Flask, render_template

from database import db


app = Flask(__name__)

audio_dir = 'static/audio'
os.makedirs(audio_dir, exist_ok=True)

tree_dir = 'static/tree'
os.makedirs(tree_dir, exist_ok=True)


@app.route('/')
def main():
    raw_texts = db.texts.find().sort('created', -1)

    texts = list()
    for text in raw_texts:
        formatted = deepcopy(text)

        identifier = text['_id']
        audio_file = f'{tree_dir}/{identifier}.wav'
        if identifier not in os.listdir(tree_dir):
            with open(audio_file, 'wb') as audio_bin:
                audio_bin.write(text['audio_bin'])
        formatted['audio'] = audio_file

        print(text['created'].replace(tzinfo=timezone.utc))
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

    return render_template('data.html', texts=texts)


if __name__ == '__main__':
    app.run(debug=True)
