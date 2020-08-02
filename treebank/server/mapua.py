import re


from const import COURSES, ROOMS, ABBR, TERMS, ENTITIES

def preprocess(sentence: str) -> str:
    for phrase in set(COURSES + ROOMS + ABBR + TERMS):
        pattern = re.compile(phrase, re.IGNORECASE)
        results = re.findall(pattern, sentence)

        if results:
            transform = [(result, re.sub(' ', '-', result))
                         for result in results]

            for old, new in transform:
                sentence = re.sub(old, new, sentence)

    return sentence


def tag_entities(tagged_words: tuple) -> list:
    ne_tags = list()
    for word, tag in tagged_words:
        entity = ENTITIES.get(word.upper())

        if entity:
            ne_tags.append((entity, word))

    return ne_tags
