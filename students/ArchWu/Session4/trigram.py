#!/usr/bin/env python3

words = "I wish I may I wish I might".split()


def build_trigrams(words):
    """
    build up the trigrams dict from the list of words

    returns a dict with:
       keys: word pairs
       values: list of followers
    """
    trigrams = {}
    words = words.split()
    for i in range(0, len(words - 2)):
        word1 = words[i]
        word2 = words[i + 1]
        word3 = words[i + 2]
        trigrams[(word1, word2)] = word3

    # build up the dict here!

    return trigrams


if __name__ == "__main__":
    trigrams = build_trigrams(words)
    print(trigrams)
