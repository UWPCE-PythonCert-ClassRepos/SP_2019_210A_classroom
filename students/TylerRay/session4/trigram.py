import random
import sys
from itertools import islice

def make_words():
    '''
    make a list of words from text
    strips all punctuation
    '''

    replace_punc = [('-', ' '),
                    (',', ''),
                    (',', ''),
                    ('.', ''),
                    (')', ''),
                    ('(', ''),
                    ('"', '')]

    # translation table
    table = {}
    for orig, replace in replace_punc:
        table[ord(orig)] = replace
    text = text.translate(table)
    # lower-case everything
    text = text.lower()

    # split into words
    words = text.split()

    # remove teh bare single quotes and cap 'i'
    words2 = []
    for word in words:
        if word != "'":
            words2.append("I" if word =='i' else word)
    return words2


def read_file(filename):
    '''
    Reads the file and return one big stream
    :param filename: the file to be opened
    :return: big string
    '''

    words = []
    with open(filename) as text:
        for line in text:
            words.extend(line.split())
    return words


def build_trigrams(words):
    '''buil a trigram dict from passed in words'''
    trigrams = {}
    #pairs = []
    for ind in range(len(words)-2):
        w1 = words[ind]
        w2 = words[ind + 1]
        w3 = words[ind + 2]
        pairs = (w1, w2)
        if pairs not in trigrams:
            trigrams[pairs] = [w3]
        else:
            trigrams[pairs].append(w3)
    return trigrams


def build_new_text(trigrams):
    x = trigram_construction()

    new_text = []
    new_sentence = list(random.choice(list(trigrams.keys)))

    for i in range(random.randint(2,10)):
        pair = tuple(new_sentence[-2:])
        new_sentence.append(random.choice(trigrams[pair]))

        new_sentence[0] = new_sentence[0].capitalize()

        new_sentence[-1] += '.'
        new_text.extend(new_sentence)
    new_text = ' '.join(new_text)

    return new_text


if __name__ == '__main__':

    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    filename = "sherlock_small.txt"
    in_data = read_file(filename)
    words - make_words(in_data)
    trigrams = build_trigrams(words)
    new_text = build_new_text(trigrams)

    print(new_text)