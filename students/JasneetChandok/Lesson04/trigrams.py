#!/usr/bin/env python3

"""Lesson 4: Trigrams Lab

Note: Have refrenced another classmates solution

"""

import random

punctuations = "!" + "-" + "," + "." + "(" + ")" + '"' + '?' + ';' + ":" + '\n'
replacements = " " * 11


def read_file(filename):
    words = []
    with open(filename, "r") as text:
        for line in text.readlines():
            raw_line = line
            clean_string = raw_line.translate(raw_line.maketrans(punctuations,replacements))
            clean_text = "".join(clean_string)
            list_text = clean_text.split()
            words.extend(list_text)
    return words


def build_trigrams(words):
    trigrams = {}
    for ind in range(len(words) - 2):
        w1 = words[ind]
        w2 = words[ind + 1]
        w3 = words[ind + 2]
        pair = (w1, w2)
        if pair not in trigrams:
            trigrams[pair] = [w3]
        else:
            trigrams[pair].append(w3)
    return trigrams


def make_text(trigrams):
    new_text = []
    for i in range(10):
        sentence = list(random.choice(list(trigrams.keys())))
        for j in range(random.randint(2, 10)):
            pair = tuple(sentence[-2:])
            sentence.append(random.choice(trigrams[pair]))
        sentence[0] = sentence[0].capitalize()
        sentence[-1] += "."
        new_text.extend(sentence)
    new_text = " ".join(new_text)
    return new_text


def main():
    in_file = read_file("sherlock_small.txt")
    trigrams = build_trigrams(in_file)
    final_text = make_text(trigrams)
    print(final_text)


if __name__ == "__main__":
    main()
