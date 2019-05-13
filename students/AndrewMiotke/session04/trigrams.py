#!/usr/bin/env python3
import random

"""
Solution to trigram problem
"""

def read_file(filename):
    """
    returns a list of words in the file
    """
    words = [] # creates empty list
    with open(filename) as text:
        for line in text:
            words.extend(line.split())

    return words


def build_trigrams(word_list):
    """
    takes a list of words and makes a trigrams dict
    """
    trigrams = {}

    for ind in range(len(word_list) - 2):
        w1 = word_list[ind]
        w2 = word_list[ind + 1]
        w3 = word_list[ind + 2]
        pair = (w1, w2)

        if pair not in trigrams:
            trigrams[pair] = [w3]
        else:
            trigrams[pair].append(w3)

    return trigrams


def create_sentence(trigram):
    sentence = []
    starting_key = random.choice(list(trigram.keys()))
    sentence.extend([word for word in starting_key])
    sentence.append(trigram[starting_key][random.choice(range(0, len(trigram[starting_key])))])

    while len(sentence) < 15:
        try:
            key1, key2 = sentence[-2:]
            sentence.append(trigram[(key1, key2)][random.choice(range(0, len(trigram[(key1, key2)])))])
        except KeyError:
            break

    sentence[0] = sentence[0].capitalize()
    if sentence[-1][-1] != ".":
        sentence[-1] = f"{sentence[-1]}."
    return sentence


def create_paragraph(trigram):
    paragraph = []
    while len(paragraph) <= 5:
        paragraph.append(create_sentence(trigram))
    return paragraph


def create_new_text(text):
    for paragraph in text:
        for sentence in paragraph:
            for word in sentence:
                print(word, end=' ')
            print()
        print()


def create_trigram():
    # Small text
    import_words_from = read_file("sherlock_small.txt")

    # Full Sherlock book(large text)
    # import_words_from = read_file("sherlock.txt")
    trigram = (build_trigrams(import_words_from))

    new_trigram = []
    for _ in range(20):
        new_trigram.append(create_paragraph(trigram))

    create_new_text(new_trigram)


if __name__ == "__main__":
    create_trigram()