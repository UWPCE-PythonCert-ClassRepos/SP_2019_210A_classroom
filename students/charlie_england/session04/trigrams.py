#!/usr/bin/env python
import random
"""
Solution for trigrams problem
"""

def read_file(filename):
    """
    :returns: list of words in the file
    """
    #need to clean up input including punctuation
    ln_lst = []
    with open(filename) as text:
        for line in text:
            ln_lst.extend(line.split()) #extend will add to the original list instead of adding a new list
        return ln_lst
            

def build_trigrams(words):
    #make 2 copies of list and zip them together?
    """
    Takes a list of words and makes a trigrams dict
    """
    trigrams = {}
    ind = 0
    for _ in range(len(words)-2):
        w1 = words[ind]
        w2 = words[ind+1]
        w3 = words[ind+2]
        pair = (w1, w2)
        #pair = f"{w1} {w2}" #creates a string variable called pair with the format "word1 word2"
        ind+=1
        if pair in trigrams:
            trigrams[pair].append(w3)
        else:
            trigrams.update({pair:[w3]})
    return trigrams

def make_text(trigrams):
    """
    1) pick a random pair of words to start with
    2) pick a random list of following words to choose from
    3) from the new random word added, pick w2+w3 as the next words to start with
    """
    rtrn_lst = []
    start = random.choice(list(trigrams.keys()))
    prev_words = list(start)
    rtrn_lst.extend(start)
    for _ in range(20):
        r_choice = random.choice(trigrams[prev_words])
        rtrn_lst.extend(r_choice)
        prev_words.append(r_choice)
        print(rtrn_lst)
    

words = read_file("sherlock_small.txt")
trigram = build_trigrams(words)
print(make_text(trigram))
