#Trigrams
#FredBallyns
#Session04

"""
Creates 10 paragraphs each one sentence long.
Starts first sentence with Sherlock Holmes.
It accounts for some of the cases where a decimal is not actually the end of a sentence, but not all.
Code accounts for potential end of trigrams error by looping back to the start
"""

import random

#WORDS = "I wish I may I wish I might. I like I wish I need? I want I may I like".split()

def read_file(filename):
    """
    :returns: list of words in the file
    """
    lines=[]
    with open(filename) as text:
        for line in text:
            lines.append(line)
    return str(" ".join(lines))

def make_words(in_data):
    remove_these = ("(", ")", "[", "]", '"', " '", "' ")
    for i in remove_these:
        in_data = in_data.replace(i, "")
    replace_these = ("\n", "-", "  ")
    for i in replace_these:
        in_data = in_data.replace(i, " ")    
    return in_data.split()

def build_trigrams(words):
    """
    takes a list of words and makes a trigram dict
    """
    trigrams = {}
    for ind in range(len(words) - 2):
        word1 = words[ind]
        word2 = words[ind + 1]
        word3 = words[ind + 2]
        trigrams.setdefault((word1, word2), []).append(word3)
    #Creates loop avoid end of file error even if makes no sense
    trigrams.setdefault((word2, word3), []).append(words[0])
    trigrams.setdefault((word3, words[0]), []).append(words[1])
    return trigrams
	
def build_text(trigrams):
    prior_pair = ("Sherlock", "Holmes")
    new_text=" ".join(prior_pair)
    #Create 10, one sentence paragraphs
    for i in range(10):
        incomplete_sentence = True
        while incomplete_sentence == True:
            next_word = random.choice(trigrams[prior_pair])
            prior_pair = (prior_pair[1],next_word)
            new_text += " " + next_word
            #Sentence ends with one of three characters
            if not (next_word.lower()=="dr." or next_word.lower()=="mr." or next_word.lower()=="mrs." or next_word.lower()=="ms." or next_word.lower()=="st.") and (next_word[-1] == "." or next_word[-1] == "?" or next_word[-1] == "!"):
                incomplete_sentence = False
                new_text += "\n \n"
    return " "+ new_text


if __name__ == "__main__":
    # run a tests
    in_data = read_file("sherlock.txt")
    words = make_words(in_data)
    trigrams = build_trigrams(words)
    new_text = build_text(trigrams)
    print(new_text)