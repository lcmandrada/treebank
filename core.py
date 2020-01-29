import os

from nltk import Nonterminal, induce_pcfg, InsideChartParser
# from nltk.draw import TreeWidget
# from nltk.draw.util import CanvasFrame
from nltk.parse.corenlp import CoreNLPServer
from nltk.parse import CoreNLPParser
from nltk.tokenize import sent_tokenize

from speech import speech_to_text


text = speech_to_text('harvard.wav', length=2000, thresh=-32)
print(text)

STANFORD = 'stanford-corenlp-full-2018-10-05'

jars = (
    os.path.join(STANFORD, 'stanford-corenlp-3.9.2.jar'),
    os.path.join(STANFORD, 'stanford-corenlp-3.9.2-models.jar')
)

with CoreNLPServer(*jars):
    parser = CoreNLPParser(tagtype='pos')
    sentences = sent_tokenize(text)

    for sentence in sentences:
        tokenized = list(parser.tokenize(sentence))
        print(f'Tokenized: {tokenized}')

        tagged = list(parser.tag(tokenized))
        print(f'Tagged: {tagged}')

        parsed = next(parser.raw_parse(sentence))
        print('Grammar')
        parsed.pretty_print()

        root = Nonterminal('S')
        grammar = induce_pcfg(root, parsed.productions())
        print(grammar)

        parser = InsideChartParser(grammar)
        for tree in parser.parse(tokenized):
            print(tree)

        # parser = nltk.ViterbiParser(grammar)
        # parser = nltk.RandomChartParser(grammar)
        # parser = nltk.UnsortedChartParser(grammar)
        # parser = nltk.LongestChartParser(grammar)

        # cf = CanvasFrame()
        # tc = TreeWidget(cf.canvas(), parsed)
        # tc['node_font'] = 'arial 14 bold'
        # tc['leaf_font'] = 'arial 14'
        # tc['node_color'] = '#005990'
        # tc['leaf_color'] = '#3F8F57'
        # tc['line_color'] = '#175252'
        # cf.add_widget(tc, 20, 20)
        # cf.print_to_file(f'tree_{tokenized[0]}.ps')
        # cf.destroy()
        # os.system(f'convert tree_{tokenized[0]}.ps tree_{tokenized[0]}.png')
