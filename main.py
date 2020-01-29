import nltk


from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize, sent_tokenize


# set of english words
# words = set(nltk.corpus.words.words())

text = "What is the airspeed of an unladen swallow?"
sentences = sent_tokenize(text)

words = list()
tags = list()

for sentence in sentences:
    # word segmentation
    tokens = word_tokenize(sentence)
    words.append(tokens)

    tags.append(pos_tag(tokens))

print(words)
print(tags)

# nltk.help.upenn_tagset()
