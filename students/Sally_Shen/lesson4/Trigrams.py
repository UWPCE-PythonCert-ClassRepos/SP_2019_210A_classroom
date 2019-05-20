'''
The trigrams
'''

import re

def read_file(filename):
    '''

    return the words in the text
    '''

    words = []
    with open (filename, "r") as text:
        firstLine = True
        for line in text:
            if firstLine:
                line = re.sub("--.*--", " ", line)
                firstLine = False
            print(line)
            line = line.replace(",", "")
            words.extend(line.split())
    return words


def build_trigrams(words):
    '''
    a list of words and make a trigrams dict
    '''

    trigrams = {}
    for ind in range(len(words)-2):
        w1 = words[ind]
        w2 = words[ind + 1]
        w3 = words[ind + 2]
        pair = (w1, w2)
        if pair not in trigrams:
            trigrams[pair] = [w3]
        else:
            trigrams[pair].append(w3)

    #print(trigrams)
    return trigrams

def make_text(trigrams):
    output = ""
    currentIndex = {}
    pair = list(trigrams.keys())[0]
    output += " ".join(pair)
    value = trigrams[pair]

    while pair in trigrams and (pair not in currentIndex or currentIndex[pair] < len(value) - 1):
        if pair not in currentIndex:
            currentIndex[pair] = 0
        #print(pair)
        valueIndex = currentIndex[pair]
        value = trigrams[pair]
        output += " " + value[valueIndex]

        currentIndex[pair] = currentIndex[pair] + 1
        pair = (pair[1], value[valueIndex])
        #print(output)
    return output

words = read_file("sherlock_small.txt")
trigrams = build_trigrams(words)
output = make_text(trigrams)
#print(words)
#print(trigrams)
print(output)

# trigrams = {("I", "wish"): ["I", "I"],
#             ("wish", "I"): ["may", "might"],
#             ("may", "I"): ["wish"],
#             ("I", "may"): ["I"],}