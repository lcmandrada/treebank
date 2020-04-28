from datetime import datetime

from bson import Binary
from flask import Flask, request, jsonify

from database import db
from parser import parse
from speech import speech_to_text


app = Flask(__name__)


def run(audio_path: str = 'test.wav', min_length: int = 1000,
        db_threshold: int = -32, speech_api: str = 'sphinx') -> list:
    text = speech_to_text(audio_path, min_length=min_length,
                          db_threshold=db_threshold, speech_api=speech_api)
    print(f'Speech to text: {" ".join(t for t, a in text)}\n')

    for text_audio in text:
        results = dict()

        sentence, chunk = text_audio
        index = chunk.split('_')[1].split('.')[0]
        with open(chunk, 'rb') as chunk_bin:
            results['audio_bin'] = Binary(chunk_bin.read())

        results.update(parse(sentence, index=index))

        results['created'] = datetime.now()
        db.texts.insert_one(results)


@app.route('/', methods=['POST'])
def main():
    payload = request.get_json()
    run(**payload)
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
