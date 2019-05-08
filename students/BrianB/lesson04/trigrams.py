#! bin/usr/env python3


def read_file(filename):
    """return: list of words in the file"""

    words = []
    with open('sherlock_small.txt') as text:
        for line in text:
            words.extend(line.replace("--", " ").split())
    return words


def build_trigrams(words):
    """takes a list of words and makes a trigram dictionary"""

    trigrams = {}
    for ind in range(len(words) - 2):
        w1 = words[ind]
        w2 = words[ind + 1]
        w3 = words[ind + 2]
        pair = (w1, w2)
        if pair not in trigrams:
            trigrams[(w1, w2)] = [w3]
        else:
            trigrams[pair].append(w3)
    return trigrams


def print_trigram():
    """take a trigram dictionary and returns the trigram"""
    trig = build_trigrams(words)
    list_trig = list(trig.items())
    for key, value in list_trig:
        print(key, value)


words = read_file("/Users/brianbrumleve/SP_2019_210A_classroom/students/\
    BrianB/lesson04/sherlock_small.txt")


if __name__ == "__main__":

    print_trigram()
