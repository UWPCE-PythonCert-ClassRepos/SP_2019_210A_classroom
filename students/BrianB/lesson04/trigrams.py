#! bin/usr/env python3

'''
solutions to trigrams problem
'''
'''
WORDS = "with his head sunk upon his chest and\
 his hands clasped behind him".split()
'''
# WORDS = "I wish I may I wish I might".split()


def read_file(filename):
    '''
    return: list of words in the file
    '''
    words = []
    with open(filename) as text:
        for line in text:
            # print(line)
            words.extend(line.split())
    return words


def build_trigrams(words):
    '''
    takes a list of words and makes a trigram dictionary
    '''
    trigrams = {}
    # pairs = []
    for ind in range(len(words) - 2):
        w1 = words[ind]
        w2 = words[ind + 1]
        w3 = words[ind + 2]
        # pair = " ".join((w1, w2))
        pair = (w1, w2)
        if pair not in trigrams:
            trigrams[(w1, w2)] = [w3]
        else:
            trigrams[pair].append(w3)
        # print(W1, w2, w3)

    return trigrams


words = read_file("/Users/brianbrumleve/SP_2019_210A_classroom/students/\
BrianB/lesson04/Trigram text samples/sherlock_small.txt")
# print(words)
trigrams = build_trigrams(words)
print(trigrams)
