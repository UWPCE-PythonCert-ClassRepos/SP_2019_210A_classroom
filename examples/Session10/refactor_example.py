"""
An example of refactoring code to make it correct and cleaner.

This is from part of the trigrams exercise: removing punctuation
for a list of words
"""

import string

# the original version:

#make words - avoid punctuation and capital letters
def make_words(d1):
    pnc = set(string.punctuation)

    #replace punctuation to empty
    for x in range (len(d1)):
        if d1[x] != 'I':
            d1[x] = d1[x].lower()
        for w1 in pnc:
            d1[x] = d1[x].replace(w1, '')
    return d1


# def clean_words(word_list):
#     """
#     clean up word list

#     removes capitalization and punctuation from a list of words

#     :param word_list: list of individual words

#     :returns: list of cleaned up words
#     """
#     for i in range(len(word_list)):
#         for punc in string.punctuation:
#             word_list[i] = word_list[i].replace(punc, '')
#         if word_list[i] != 'I':
#             word_list[i] = word_list[i].lower()
#     return word_list


# def clean_words2(word_list):
#     """
#     clean up word list

#     removes capitalization and punctuation from a list of words

#     :param word_list: list of individual words

#     :returns: list of cleaned up words
#     """
#     new_words = []
#     for word in word_list:
#         for punc in string.punctuation:
#             word = word.replace(punc, '')
#         if word != 'I':
#             word = word.lower()
#         new_words.append(word)
#     return new_words


# def clean_word(word):
#     """
#     clean up a single word

#     removes punctuation and capitalization
#     """
#     for punc in string.punctuation:
#         word = word.replace(punc, '')
#     if word != 'I':
#         word = word.lower()
#     return word


# def clean_words3(word_list):
#     """
#     clean up word list

#     removes capitalization and punctuation from a list of words

#     :param word_list: list of individual words

#     :returns: list of cleaned up words
#     """
#     return [clean_word(word) for word in word_list]


# ##################
# now some tests -- keeping it in the same file for convenience

line1 = '''"Quite so! You have not observed. And yet you have seen. That is'''
clean1 = ['quite', 'so', 'you', 'have', 'not', 'observed', 'and',
          'yet', 'you', 'have', 'seen', 'that', 'is']

line2 = '''"My dear Holmes," said I, "this is too much.'''
clean2 = ["my", "dear", "holmes", "said", "I", "this", "is", "too", "much"]

line3 = '''"How many? I don't know."'''
clean3 = ["how", "many", "I", "dont", "know."]


def test_clean1():
    assert make_words(line1.split()) == clean1

# def test_clean2():
#     assert make_words(line2.split()) == clean2


# def test_clean3():
#     assert make_words(line3.split()) == clean3

