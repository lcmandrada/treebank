import argparse

from datetime import datetime

from bson import Binary

from database import db
from parser import parse
from speech import speech_to_text


# arguments configuration
parser = argparse.ArgumentParser(description='Mapúa Treebank')
parser.add_argument('audio_path', type=str, help='Audio path')
parser.add_argument('-m', '--min_length', type=int,
                    default=2000, help='Silence min length')
parser.add_argument('-d', '--db_threshold', type=int,
                    default=-32, help='Silence dB treshold')
parser.add_argument('-s', '--save_image', action='store_true',
                    help='Save tree as image')
args = parser.parse_args()

# convert audio input to text
text = speech_to_text(args.audio_path, length=args.min_length,
                      thresh=args.db_threshold)
print(f'Speech to text: {" ".join(t for t, a in text)}\n')


for text_audio in text:
    results = dict()

    sentence, chunk = text_audio
    index = chunk.split('_')[1].split('.')[0]
    with open(chunk, 'rb') as chunk_bin:
        results['audio_bin'] = Binary(chunk_bin.read())

    results.update(parse(sentence, args.save_image, index))

    results['created'] = datetime.now()
    db.texts.insert_one(results)
