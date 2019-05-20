

#WORDS = "with his head sunk upon his chest and his hands clasped behind him".split()


def read_file(filename):
    """"
    :returns: list of words in the file
    """
    words = []
    with open(sherlock_small.txt) as text:
        for line in text:
            print(line)
            words.extend(line.split())
    return words

#words = read_file("sherlock_small.txt")
#print(words)


def build_trigrams(words):
    """
    takes a list of words and makes a trigrams dict
    """
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
        trigrams[(w1, w2)]
    return trigrams


