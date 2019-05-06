#!/usr/bin/env python
import random
"""
Solution for trigrams problem
"""

def read_file(filename):
    """
    :returns: list of words in the file and removes any non-alpha-numeric item
    #need to update with the - and -- that are in lines
    """
    #need to clean up input including punctuation
    ln_lst = []
    alpha_num = "abcdefghijklmnopqrstuvwxyz0123456789-."
    with open(filename) as text:
        for line in text:
            line = line.split()
            for word in line:
                only_alpha_word = []
                for char in word:
                    if char in alpha_num or char in alpha_num.upper():
                        only_alpha_word.append(char.lower())
                ln_lst.append("".join(only_alpha_word))
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
        if pair in trigrams: #check to see if key is already in dictionary and update with new word if so
            trigrams[pair].append(w3)
        else:
            trigrams.update({pair:[w3]}) #if key is not in dictionary, make a new key:value pair
    return trigrams

def make_text(trigrams):
    """
    1) pick a random pair of words to start with
    2) pick a random list of following words to choose from
    3) from the new random word added, pick w2+w3 as the next words to start with
    """
    rtrn_lst = []
    k_words = list(random.choice(list(trigrams.keys())))
    rtrn_lst.extend(k_words)
    for _ in range(500):
        r_choice = random.choice(trigrams[tuple(k_words)])
        k_words.pop(0)
        k_words.append(r_choice)
        rtrn_lst.append(k_words[1])
    return " ".join(rtrn_lst)
    

if __name__ == "__main__":
    words = read_file("sherlock.txt")
    trigram = build_trigrams(words)
    print(make_text(trigram))
