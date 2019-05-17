#!/usr/bin/env python3
import random
import string

words = "I wish I may I wish I might".split()
trigrams = {}

def build_trigram(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """

    #words = words.split()
    for i in range(0, len(words) - 3):
        word1 = words[i]
        word2 = words[i + 1]
        word3 = words[i + 2]
        pair = (word1, word2)
        if pair not in trigrams:
            trigrams[(word1, word2)] = [word3]
        else:
            trigrams[(word1, word2)].append(word3)
    # build up the dict here!

    return trigrams

# def make_words(in_data):
#
#     return

def read_in_data(filename):
    """
    read the file
    :returns: list of works in the file
    """
    in_data = []
    with open(filename) as f:
        for line in f:
            for word in line.split():
                in_data.append(word)
    #f.close()
    return in_data

def build_text(word_pairs):
    initial_random = random.randint(0, len(word_pairs) - 1)
    length_limit = 1000
    word_count = 0
    text = []
    # for i, word_pair, val in enumerate(word_pairs):
    #     if i == initial_random:
    #         initial_pair = word_pair
    #         initial_word = val
    #         text.append(word_pair)
    #         text.append(val)
    #         break
    initial_pair = random.choice(list(word_pairs))
    initial_val = random.choice(word_pairs[initial_pair])
    text.extend(initial_pair)
    text.append(initial_val)

    while(word_count < length_limit):
        new_pair = (text[-2], text[-1])
        new_val = random.choice(word_pairs[new_pair])
        text.append(new_val)
        word_count += 1
    return ' '.join(text)

if __name__ == "__main__":
    # get the filename from the command line
    try:
        filename = 'sherlock.txt'
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    word_pairs = build_trigram(in_data)
    new_text = build_text(word_pairs)

    print(new_text)
