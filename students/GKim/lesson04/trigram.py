
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
    returns list of words in the file
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

# def make_text(trigrams):
#     pass


def main():
    # read_file("test.txt")
    words = read_file("test.txt")
    # print(words)
    trigrams = build_trigrams(words)
   
    print(trigrams)
    for k, v in trigrams.items():
        print(k, v)

if __name__ == "__main__": main()