
# WORDS = "with his head sunk upon his chest and his hands clasped behind him.".split()
# WORDS = "I wish I may I wish I might".split()

import random

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
    returns list of words in the file clear of unwanted punctuations
    """
    words = []
    with open(filename,"r") as text:
        for line in text.readlines():
            raw_line = line
            clean_string = punctuation_removal(raw_line,punctuations,replacements)
            clean_text = "".join(clean_string)
            list_text = clean_text.split()
            # print(list_text)
            # words.append(list_text)

            # print(line)
            words.extend(list_text)
    # print(words)
    return words

def build_trigrams(words):
    """
    takes a list of words and makes a trigrams dict
    """
    trigrams = {}
    for ind in range(len(words) - 2):
        w1 = words[ind]
        w2 = words[ind + 1]
        w3 = words[ind + 2]
        # pair = " ".join((w1, w2))
        pair = (w1, w2)
        if pair not in trigrams:
            trigrams[pair] = [w3]
        else:
            trigrams[pair].append(w3)
        # print(w1, w2, w3)

    return trigrams

def make_text(trigrams):
    """
    Chris's solution
    """

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
    in_file = read_file("sherlock_small.txt")
    # print(words)
    trigrams = build_trigrams(in_file)
    final_text = make_text(trigrams)
   
    print(final_text)

if __name__ == "__main__": main()