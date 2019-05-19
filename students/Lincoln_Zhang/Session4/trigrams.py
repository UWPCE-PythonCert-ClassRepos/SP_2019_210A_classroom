#!/usr/bin/env python3
#
#Trigrams
#http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/
#
#
#
import random,sys

from itertools import islice

# words = "I wish I may I wish I might".split()

# for w in zip(words,islice(words,1,None),islice(words,2,None)):
#     print(w)


def read_file(fname):
    """
    transfer the content of a text file to one list
    """
    words = []
    with open(fname) as f:
        for line in f:
            line = line.replace("--"," ")
            line = line.replace(",","")
            line = line.replace(".","")
            line = line.replace("(","")
            line = line.replace(")","")
            words.extend(line.split())
    return words

# RUN: "python trigrams.py sherlock_small.txt"
# comment next line off to run pytest -v
words = read_file(fname=sys.argv[1])

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
    """
    return the trigram pairs randomly
    """
    trigrams = build_trigram(words)
    k_list = []
    for k,v in trigrams.items():
        k_list.append(k)
    
    s = random.choice(k_list)
    a,b = s
    print(a,b,trigrams[s])


    # print(k_list)
    # print(trigrams)
    # i = 0
    # while (len(words) - i):
    #     s = random.choice(k_list)
    #     a,b = s
    #     print(a,b,random.choice(trigrams[s]))
    #     i += 1


if __name__ == "__main__":
    text_gen()