#!/usr/bin/env python3
import random
import string

words = "I wish I may I wish I might".split()

def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    #words = words.split()
    for i in range(0, len(words) - 2):
        word1 = words[i]
        word2 = words[i + 1]
        word3 = words[i + 2]
        if (word1, word2) not in trigrams:
            trigrams[(word1, word2)] = [word3]
        else:
            trigrams[(word1, word2)].append(word3)


    # build up the dict here!

    return trigrams

def make_words(in_data):

def read_in_data(filename):

def build_text():


if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)
