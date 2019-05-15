import random

# trigram problem


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


d1 = {}


def build_trigrams(words):
    for ind in range(len(words) - 2):
        w1 = words[ind]
        w2 = words[ind + 1]
        w3 = words[ind + 2]
        pair = (w1, w2)
        if pair not in d1:
            d1[pair] = [w3]
        else:
            d1[pair].append(w3)
    return d1


trigram_boi = build_trigrams(read_file())


def seed_next_one(seed):  # returns a third item given a dictionary key
    product_list = [random.choice(trigram_boi[seed])]  # list, finds third item using key/seed

    new_key = (seed[1], product_list[0])  # tuple, made from second part of key/seed and the new third item

    if new_key not in trigram_boi:
        return product_list[:len(list(trigram_boi))]

    product_list += seed_next_one(new_key)

    return product_list[:len(list(trigram_boi))]


def random_seed_pls(dicc):  # returns a random key (type tuple) in the dictionary!
    this_list = []
    that_list = []
    for j in dicc:
        that_list.append(j)
    this_list.append(random.choice(that_list))
    return this_list[0]


super_table = []

a = random_seed_pls(trigram_boi)

super_table += [a[0]]

super_table += [a[1]]

super_table += seed_next_one(a)

print(super_table)

print(" ".join(super_table))



