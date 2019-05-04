


WORDS = "with his head sunk upon his chest and his hands clasped behind him.".split()
# WORDS = "I wish I may I wish I might".split()
def read_file(filename):
    """
    returns list of works in the file
    """
    words = []
    with open(filename,"r") as text:
        for line in text:
            print(line)
            words.extend(line.split())

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
    pass

words = read_file("sherlock_small.txt")
# print(words)
trigrams = build_trigrams(WORDS)
print(trigrams)
