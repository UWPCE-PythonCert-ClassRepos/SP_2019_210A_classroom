# trigram problem

sentence = 'with his head sunk upon his chest and his hands clasped behind him'.split()


def read_file():
    '''
    :return: list of words from file
    '''
    lines_list = []
    with open('sherlock_small.txt', 'r+') as text:
        for line in text:
            # print(line)
            lines_list.extend(line.split())
    return lines_list


# print(read_file())

d1 = {}


def build_trigrams(words):
    for ind in range(len(words) - 2):
        w1 = words[ind]
        w2 = words[ind + 1]
        w3 = words[ind + 2]
        pair = (w1, w2)
        if pair not in d1:
            d1[pair] = w3
        else:
            d1[pair] += w3
    return d1


#     for word in words:
#         d1[word] = ''
#     return d1


print(build_trigrams(read_file()))

# # in class
# for ind in range(len(words)-2):
#     w1 = words[ind]
#     w2 = words[ind + 1]
#     w3 = words[ind + 2]
#     pair = (w1, w2)
#     if pair not in d1:
#         d1[pair] = w3
#     else:
#         d1[pair] += w3

