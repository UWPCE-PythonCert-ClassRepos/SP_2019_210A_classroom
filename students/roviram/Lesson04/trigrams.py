#--------------------------------------------------------#
# Dev: Miguel Rovira-Gonzalez
# Week 4 Homework Assignment: Trigrams Assignment
# Changelog: Miguel Rovira-Gonzalez
#--------------------------------------------------------#

import itertools
import sys
import random

# WORDS = "with his head sunk upon his chest and his hands clasped behind him.".split()
# WORDS = "I wish I may I wish I might".split()

punctuations = "!" + "-" + "," + "." + "(" + ")" + '"' + '?' + ';' + ":" + '\n'
replacements = " " * 11


def punctuation_removal(text_line, punc, repl):
    """
    function to remove punctuations for cleaner text transition
    """
    intab = punc
    outtab = repl
    transtab = text_line.maketrans(intab, outtab)
    clean_string = text_line.translate(transtab)
    return clean_string


def read_file(filename):
    """
    Read the file and turn it into a list of words
    :param filename:
    :return: list of words in the file
    """
    words = []
    # Code wasn't working unless I put the full file path in
    with open(r"C:\Users\roviram\Python_210\SP_2019_210A_classroom\students\roviram\Lesson04\sherlock.txt") as text:
        for line in text:
            words.extend(line.split())
    return words

def build_trigrams(words):
    """
    Takes a list of words and makes a trigrams dict
    :param words:
    :return:
    """
    pairs = []
    trigrams = {}
    for index in range(len(words) - 2):
        w1 = words[index]
        w2 = words[index + 1]
        w3 = words[index + 2]
        trigrams[(w1, w2)] = [w3]
        pair = (w1, w2)
        if pair not in trigrams:
            trigrams[pair] += [w3]
        else:
            trigrams[pair].append(w3)
    return trigrams

"""
After this line, using Chris's code to finish the assignment since I got stuck here
"""
def make_text(trigrams):
    new_text = []
    for i in range(10):  # do ten sentences
        # pick a word pair to start the sentence
        # need to make dict.keys() a list to randomly select from it
        sentence = list(random.choice(list(trigrams.keys())))
        # now add a random number of additional words to the sentence
        for j in range(random.randint(2, 10)):
            pair = tuple(sentence[-2:])  # the next word pair is the last two words
            sentence.append(random.choice(trigrams[pair]))

        # capitalize the first word:
        sentence[0] = sentence[0].capitalize()

        # Add the period
        sentence[-1] += "."
        new_text.extend(sentence)

    new_text = " ".join(new_text)
    return new_text

def main():
    # read_file("test.txt")
    # read_file("test.txt")
    in_file = read_file("sherlock.txt")
    # print(words)
    trigrams = build_trigrams(in_file)
    final_text = make_text(trigrams)
    print(final_text)


if __name__ == "__main__":
    main()






