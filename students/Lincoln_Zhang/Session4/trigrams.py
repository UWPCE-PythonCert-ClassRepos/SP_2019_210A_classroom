#!/usr/bin/env python3
#
#Trigrams
#http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/
#
#
#
import random

words = "I wish I may I wish I might".split()

def read_file(fname):
    words = []
    with open(fname) as f:
        for line in f:
            words.extend(line.split())
    return words

def build_trigram(words):
    """
    Build up the trigrams dict from the list of words
    return a dict with
    keys: word pairs
    value: list of followers
    """
    trigrams = {(words[0],words[1]):[words[2]]}
    n = len(words) - 2
    for i in range(1,n):
        window = words[i:i+3]
        key = (window[0],window[1])
        value = [window[2]]
        pair = {key:value}
        d = trigrams.keys()
        if key in d:
            trigrams[key].extend(value)
        else:
            trigrams.update(pair)

    return trigrams

def text_gen():
    trigrams = build_trigram(words)
    k_list = []
    for k,v in trigrams.items():
        k_list.append(k)

    print(k_list)
    i = 0
    while (len(words) - i):
        s = random.choice(k_list)
        a,b = s
        print(a,b,random.choice(trigrams[s]))
        i += 1


if __name__ == "__main__":
    text_gen()