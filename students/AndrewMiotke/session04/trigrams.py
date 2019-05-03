#!/usr/bin/env python3
import random

"""
Solution to trigram problem
"""

# WORDS = "I was seized with a keen desire to see Holmes again, and to know how he was employing his extraordinary powers.".split()
WORDS = "I wish I may I wish I might".split()

def read_file(filename):
    """
    returns a list of words in the file
    """
    words = [] # empty list
    with open(filename) as text:
        for line in text:
            print(line)
            words.extend(line.split())

    return words


def build_trigrams(words):
    """
    takes a list of words and makes a trigrams dict
    """
    trigrams = {}

    for ind in range(len(words) - 2):
        w1 = words[ind]
        w2 = words[ind + 1]
        w3 = words[ind + 2]

        pair = (w1, w2)
        if pair not in trigrams:
            trigrams[pair] = [w3]
        else:
            trigrams[pair].append(w3)

    return trigrams

def make_text(trigrams):
    # use random.choice()



words = read_file("sherlock_small.txt")
print(words)
trigrams = build_trigrams(WORDS)
print(trigrams)
