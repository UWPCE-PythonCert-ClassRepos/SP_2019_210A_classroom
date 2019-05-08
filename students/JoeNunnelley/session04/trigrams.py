#! /usr/bin/env python3
"""
Trigrams Progject
Author : Joe Nunnelley
"""

import random


def read_file(filename):
    """Read a file and get its words into a list"""
    words_in = []
    with open(filename, 'r') as corpus:
        words_in = corpus.read().replace('\n', ' ') \
                      .replace(':', '').replace(',', '') \
                      .replace('.', '').replace('\'', '') \
                      .split(' ')

        words_in = list(filter(None, words_in))

    return words_in


def build_trigrams(words_in):
    """
    Based on a list of words, build trigrams
    of the form [(1,2)[1,2]]
    """
    trigrams = {}
    for index in range(len(words_in) - 2):
        if words_in[index]:
            key_in = (words_in[index], words_in[index + 1])
            trigrams.setdefault(key_in, []).append(words_in[index + 2])

    return trigrams


def debug(message):
    """Output debug messages when flag set"""
    if str.lower(DEBUG_SET) == 'y':
        print("DEBUG: {}".format(message))


def generate_new_text(trigram_dict_in):
    """Create the new text from the trigram dict"""
    tri_key = random.choice(list(trigram_dict_in))
    new_text_in = " ".join(tri_key).capitalize()

    while tri_key in trigram_dict_in:
        debug("Current Key: {}".format(tri_key))
        next_word = random.choice(trigram_dict_in[tri_key])
        leading_char = " "
        if str.isupper(next_word[0:1]):
            leading_char = ". "

        new_text_in = leading_char.join([new_text_in, next_word])
        tri_key = (tri_key[1], next_word)

    print('\n\n####Generation Complete.####\n\n')

    return new_text_in + "."


if __name__ == "__main__":
    DEBUG_SET = input('Run in debug? (Y|N) :>')
    WORDS = read_file(input('Process File :> '))

    for _ in WORDS:
        if not _:
            print("Empty word found")

    debug("{} words processed".format(len(WORDS)))

    TRIGRAM_DICT = build_trigrams(WORDS)

    for key, value in TRIGRAM_DICT.items():
        debug("{} => {}".format(key, value))

    NEW_TEXT = generate_new_text(TRIGRAM_DICT)

    print(NEW_TEXT)
