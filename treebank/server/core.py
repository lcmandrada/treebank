import argparse

from datetime import datetime

from bson import Binary

from database import db
from parser import parse
from speech import speech_to_text


parser = argparse.ArgumentParser(description='Mapúa Treebank')
parser.add_argument('audio_path', type=str, help='Audio path')
parser.add_argument('-m', '--min_length', type=int,
                    default=1000, help='Silence min length')
parser.add_argument('-d', '--db_threshold', type=int,
                    default=-32, help='Silence dB treshold')
parser.add_argument('-s', '--save_image', action='store_true',
                    help='Save tree as image')
parser.add_argument('-a', '--speech_api', type=str,
                    default='sphinx', help='Speech API')
args = parser.parse_args()


def run(audio_path: str, min_length: int = 1000, db_threshold: int = -32,
        speech_api: str = 'sphinx'):
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


if __name__ == '__main__':
    run(args.audio_path, min_length=args.min_length,
        db_threshold=args.db_threshold, speech_api=args.speech_api)
