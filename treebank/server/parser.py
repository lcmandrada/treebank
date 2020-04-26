import re
import os
import uuid

from functools import reduce
from operator import mul
from shutil import rmtree

import nltk
from bson import Binary
from nltk import Nonterminal, induce_pcfg, ne_chunk
from nltk.draw import TreeWidget
from nltk.draw.util import CanvasFrame
from nltk.parse import CoreNLPParser


# stanford parser
pos_parser = CoreNLPParser(url='http://localhost:9000', tagtype='pos')

# tree dir
trees_path = 'tree'
if os.path.exists(trees_path):
    rmtree(trees_path)
os.mkdir(trees_path)


def save_image(parsed, index: str) -> Binary:
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
    os.remove(f'{trees_path}/tree_{index}.ps')
    with open(f'{trees_path}/tree_{index}.png', 'rb') as tree_img:
        tree_bin = Binary(tree_img.read())

    return tree_bin


def parse(sentence: str, save: bool = False,
          index: str = str(uuid.uuid4())) -> dict:
    results = dict()

    print(f'Sentence: {sentence}')
    results['speech_text'] = sentence

    tokenized = list(pos_parser.tokenize(sentence))

    print(f'Tokenized: {tokenized}')
    print(f'Total words: {len(tokenized)}\n')

    tagged = list(pos_parser.tag(tokenized))
    print(f'Tagged: {tagged}\n')
    results['pos_tagged'] = tagged

    ne_tags = ne_chunk(tagged)
    entities = [(tag.label(), ' '.join(t[0] for t in tag))
                for tag in ne_tags if hasattr(tag, 'label')]
    print(f'Entities: {entities}\n')
    results['named_entities'] = entities

    parsed = next(pos_parser.raw_parse(sentence))
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

    if save:
        results['tree_bin'] = save_image(parsed, index)

    return results
