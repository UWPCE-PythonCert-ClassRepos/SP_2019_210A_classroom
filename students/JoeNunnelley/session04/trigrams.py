#! /usr/bin/env python3

import random

def read_file(filename):
    words = []
    with open(filename, 'r') as corpus:
        words = corpus.read().replace('\n', ' ').replace(':', '').replace(',', '').replace('.', '').replace('\'','').split(' ')
        words = list(filter(None, words))

    return words

def build_trigrams(words):
    trigrams = {}
    for index in range(len(words) - 2):
        if words[index]:
            key = (words[index], words[index + 1])

            if key in trigrams.keys():
                trigrams[key].append(words[index + 2])
            else:
                trigrams[key] = [ words[index + 2] ]

    return trigrams

def generate_new_text(trigram_dict):
    while len(trigram_dict) > 0:
        tri_key = random.choice(list(trigram_dict))
        print("Current Key: {} Values: {}".format(tri_key, trigram_dict[tri_key]))
        new_text = " ".join(tri_key)
        value_set = trigram_dict[tri_key]

        while len(value_set) > 0:
            next_word = random.choice(trigram_dict[tri_key])
            trigram_dict[tri_key].remove(next_word)
            new_text += (" {}".format(next_word))
            tri_key = (tri_key[1], next_word)
        else:
            del trigram_dict[tri_key]
    else:
        print('\n\n####Generation Complete.####\n\n')

    return new_text


if __name__ == "__main__":
    words = read_file(input('Process File :> '))

    for _ in words:
        if len(_) == 0:
            print("Empty word found")

    print("{} words processed".format(len(words)))

    trigram_dict = build_trigrams(words)

    for key, value in trigram_dict.items():
        print("{} => {}".format(key, value))

    new_text = generate_new_text(trigram_dict)

    print(new_text)