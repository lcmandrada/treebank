import argparse
import os
import re

import nltk

from nltk import Nonterminal, induce_pcfg
from nltk.draw import TreeWidget
from nltk.draw.util import CanvasFrame
from nltk.parse.corenlp import CoreNLPServer
from nltk.parse import CoreNLPParser
from nltk.tokenize import sent_tokenize

from speech import speech_to_text


# arguments configuration
parser = argparse.ArgumentParser(description='Mapua Treebank')
parser.add_argument('-a', '--audio_path', type=str,
                    default='harvard.wav', help='Audio path')
parser.add_argument('-m', '--min_length', type=int,
                    default=2000, help='Silence min length')
parser.add_argument('-d', '--db_threshold', type=int,
                    default=-32, help='Silence dB treshold')
parser.add_argument('-s', '--save_image', action='store_true',
                    help='Save tree as image')
args = parser.parse_args()

# stanford nlp configuration
STANFORD = 'stanford-corenlp-full-2018-10-05'

jars = (os.path.join(STANFORD, 'stanford-corenlp-3.9.2.jar'),
        os.path.join(STANFORD, 'stanford-corenlp-3.9.2-models.jar'))

# convert audio input to text
raw_text = speech_to_text(args.audio_path, length=args.min_length,
                          thresh=args.db_threshold)
sentences = sent_tokenize(raw_text)
text = [sent.capitalize() for sent in sentences]
print(f'Speech to text: {" ".join(text)}\n')

# text configurations
common_punct = '[,.!?]'

# start stanford nlp server
with CoreNLPServer(*jars):
    parser = CoreNLPParser(tagtype='pos')
    for index, sentence in enumerate(text):
        print(index + 1)
        raw_sentence = re.sub(common_punct, '', sentence)

        print(f'Sentence: {raw_sentence}')
        tokenized = list(parser.tokenize(sentence))
        raw_tokenized = list(parser.tokenize(raw_sentence))
        print(f'Tokenized: {raw_tokenized}')
        print(f'Total words: {len(raw_tokenized)}\n')

        tagged = list(parser.tag(tokenized))
        print(f'Tagged: {tagged}\n')

        parsed = next(parser.raw_parse(sentence))
        print('Grammar')
        parsed.pretty_print()

        root = Nonterminal('S')
        grammar = induce_pcfg(root, parsed.productions())
        print(grammar, '\n')

        grammar_parser = nltk.ViterbiParser(grammar)
        for tree in grammar_parser.parse(tokenized):
            print(tree, '\n')

        # list of parsers
        # grammar_parser = nltk.InsideChartParser(grammar)
        # grammar_parser = nltk.ViterbiParser(grammar)
        # grammar_parser = nltk.RandomChartParser(grammar)
        # grammar_parser = nltk.UnsortedChartParser(grammar)
        # grammar_parser = nltk.LongestChartParser(grammar)

        if args.save_image:
            cf = CanvasFrame()
            tc = TreeWidget(cf.canvas(), parsed)
            tc['node_font'] = 'arial 14 bold'
            tc['leaf_font'] = 'arial 14'
            tc['node_color'] = '#005990'
            tc['leaf_color'] = '#3F8F57'
            tc['line_color'] = '#175252'
            cf.add_widget(tc, 20, 20)
            cf.print_to_file(f'tree_{tokenized[0]}.ps')
            cf.destroy()
            os.system(f'convert tree_{tokenized[0]}.ps '
                      'tree_{tokenized[0]}.png')
