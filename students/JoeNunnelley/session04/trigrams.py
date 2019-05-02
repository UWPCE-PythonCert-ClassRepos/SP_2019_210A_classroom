#! /usr/bin/env python3

import random


def read_file(filename):
    """Read a file and get its words into a list"""
    words = []
    with open(filename, 'r') as corpus:
        words = corpus
                .read()
                .replace('\n', ' ')
                .replace(':', '')
                .replace(',', '')
                .replace('.', '')
                .replace('\'', '')
                .split(' ')

        words = list(filter(None, words))

    return words


def build_trigrams(words):
    """
    Based on a list of words, build trigrams
    of the form [(1,2)[1,2]]
    """
    trigrams = {}
    for index in range(len(words) - 2):
        if words[index]:
            key = (words[index], words[index + 1])

            if key in trigrams.keys():
                trigrams[key].append(words[index + 2])
            else:
                trigrams[key] = [words[index + 2]]

    return trigrams


def debug(message):
    if str.lower(debug_set) == 'y':
        print("DEBUG: {}".format(message))


def generate_new_text(trigram_dict):
    tri_key = random.choice(list(trigram_dict))
    new_text = " ".join(tri_key).capitalize()

    while tri_key in trigram_dict:
        debug("Current Key: {}".format(tri_key))
        next_word = random.choice(trigram_dict[tri_key])
        leading_char = " "
        if str.isupper(next_word[0:1]):
            leading_char = ". "

        new_text = leading_char.join([new_text, next_word])
        tri_key = (tri_key[1], next_word)
    else:
        print('\n\n####Generation Complete.####\n\n')

    return new_text + "."


if __name__ == "__main__":
    debug_set = input('Run in debug? (Y|N) :>')
    words = read_file(input('Process File :> '))

    for _ in words:
        if len(_) == 0:
            print("Empty word found")

    debug("{} words processed".format(len(words)))

    trigram_dict = build_trigrams(words)

    for key, value in trigram_dict.items():
        debug("{} => {}".format(key, value))

    new_text = generate_new_text(trigram_dict)

    print(new_text)
