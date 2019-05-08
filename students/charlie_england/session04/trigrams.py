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
        trigrams.setdefault(pair,[]).append(w3)
    return trigrams

def punc_check(word):
    puncuation = "!.?"
    if len(word) > 2:
        if word[0].lower() != "m" and (word[1].lower() != "r" or word[1].lower() != "s"):
            for letter in word:
                if letter in puncuation:
                    return 1

def make_text(trigrams,length=500):
    """
    1) pick a random pair of words to start with
    2) pick a random list of following words to choose from
    3) from the new random word added, pick w2+w3 as the next words to start with
    """
    rtrn_lst = []
    k_words = list(random.choice(list(trigrams.keys())))
    rtrn_lst.append(k_words[0].capitalize())
    rtrn_lst.append(k_words[1])
    punc = 0
    for _ in range(length):
        r_choice = random.choice(trigrams[tuple(k_words)])
        k_words.pop(0)
        k_words.append(r_choice)
        if punc == 1 or r_choice == "i": #check if there is puncuation or if the choice is i, then capitalize it
            rtrn_lst.append(r_choice.capitalize())
        else:
            rtrn_lst.append(r_choice)
        punc = 0
        punc = punc_check(r_choice) #checks the puncation in the r_choice and changes puncuation state to 1 if there is puncuation
    return " ".join(rtrn_lst)
    

if __name__ == "__main__":
    words = read_file("sherlock.txt")
    trigram = build_trigrams(words)
    print(make_text(trigram,50))
