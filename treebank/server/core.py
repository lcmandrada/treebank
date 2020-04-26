import argparse
import os
import re

from datetime import datetime
from functools import reduce
from operator import mul
from shutil import rmtree

from bson import Binary
from nltk import Nonterminal, induce_pcfg
from nltk.draw import TreeWidget
from nltk.draw.util import CanvasFrame
from nltk.parse import CoreNLPParser

from database import db
from speech import speech_to_text


# arguments configuration
parser = argparse.ArgumentParser(description='Mapua Treebank')
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

# text configurations
common_punct = '[,.!?]'

# tree dir
trees_path = 'tree'
if os.path.exists(trees_path):
    rmtree(trees_path)
os.mkdir(trees_path)

parser = CoreNLPParser(tagtype='pos', url='http://localhost:9000')
for index, text_audio in enumerate(text, 1):
    results = dict()

    sentence, chunk = text_audio
    with open(chunk, 'rb') as chunk_bin:
        results['audio_bin'] = Binary(chunk_bin.read())
    raw_sentence = re.sub(common_punct, '', sentence)

    print(f'Sentence: {sentence}')
    results['speech_text'] = sentence

    tokenized = list(parser.tokenize(sentence))
    raw_tokenized = list(parser.tokenize(raw_sentence))

    print(f'Tokenized: {raw_tokenized}')
    print(f'Total words: {len(raw_tokenized)}\n')

    tagged = list(parser.tag(raw_tokenized))
    print(f'Tagged: {tagged}\n')
    results['pos_tagged'] = tagged

    parsed = next(parser.raw_parse(raw_sentence))
    print('Grammar')
    parsed.pretty_print()

    root = Nonterminal('S')
    grammar = induce_pcfg(root, parsed.productions())
    print(grammar, '\n')

    productions = [(str(prod._lhs), [str(t) for t in prod._rhs], prod.prob())
                   for prod in grammar._productions]
    results['productions'] = productions

    probabilities = [prod.prob() for prod in grammar._productions]
    pcfg = reduce(mul, probabilities)

    print(pcfg)
    results['pcfg'] = pcfg

    if args.save_image:
        cf = CanvasFrame()
        tc = TreeWidget(cf.canvas(), parsed, xspace=40, yspace=40)
        tc['node_font'] = 'arial 20 bold'
        tc['leaf_font'] = 'arial 20 bold'
        tc['node_color'] = '#005990'
        tc['leaf_color'] = '#3F8F57'
        tc['line_color'] = '#175252'
        cf.add_widget(tc, 50, 50)

        cf.print_to_file(os.path.join(trees_path, f'tree_{index}.ps'))
        cf.destroy()

        os.system(f'convert {trees_path}/tree_{index}.ps '
                  f'{trees_path}/tree_{index}.png')
        os.remove(os.path.join(trees_path, f'tree_{index}.ps'))
        with open(f'{trees_path}/tree_{index}.png', 'rb') as tree_img:
            results['tree_bin'] = Binary(tree_img.read())

    results['created'] = datetime.utcnow()
    db.texts.insert_one(results)
