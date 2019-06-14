#!/usr/bin/env python3

import random


def read_file(input_file):
    """
    Splits an input file into a list of words
    :param input_file: a file containing words
    :return: list of words from input_file
    """
    word_list = []
    with open(input_file) as text:
        for line in text:
            if '***' not in line:
                words_from_line = line.split()
                for word in words_from_line:
                    word_list.extend([word.replace('\"', '')])
    return word_list


def build_trigrams(word_list):
    """
    Constructs a dictionary of trigrams
    :param word_list:
    :return: dict of trigrams
    """
    trigrams = {}
    for index in range(len(word_list) - 2):
        w1 = word_list[index]
        w2 = word_list[index + 1]
        w3 = word_list[index + 2]
        pair = (w1, w2)
        if pair not in trigrams:
            trigrams[pair] = [w3]
        else:
            trigrams[pair].extend([w3])
    return trigrams



def make_text(trigrams):
    """
    Constructs text from trigrams
    :param trigrams: dict
    :return: str of constructed text
    """
    pass


def main(input_file):
    """
    Generates new text from an input file using trigrams
    :param input_file: location of a file containing text
    :return: None
    """
    word_list = read_file(input_file)
    trigrams = build_trigrams(word_list)
    next_tuple = generate_tuple(word_list)
    new_text = ''
    while len(new_text) < 500:
        try:
            new_word = random.choice(trigrams[next_tuple])
        except KeyError:
            next_tuple = generate_tuple(word_list)
            continue
        if len(new_text) == 0:
            new_text += "{}".format(str.capitalize(new_word))
        elif new_text[-1] in "!?.":
            new_text += "  {}".format(str.capitalize(new_word))
        else:
            new_text += " {}".format(new_word)
        next_tuple = (next_tuple[1], new_word)
    new_text += '.'
    print(new_text)


def generate_tuple(word_list):
    """
    Generates a tuple of two random words
    :param word_list: list of one word strings
    :return: tuple of two random words
    """
    s1 = random.choice(word_list)
    s2 = random.choice(word_list)
    return (s1, s2)


if __name__ == "__main__":
    try:
        file_name = input("Provide the location of an input text file.")
        main(file_name)
    except NameError:
        print("Must be run with python 3")