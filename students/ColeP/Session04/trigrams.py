import random

# trigram problem


def read_file():
    '''
    :return: list of words from file
    '''
    lines_list = []
    with open('wishI.txt', 'r+') as text:
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
            d1[pair] = [w3]
        else:
            d1[pair].append(w3)
    return d1


trigram_boi = build_trigrams(read_file())

print(trigram_boi)
print('^good trigram\n')
print(read_file())
print('table of the line\n')
print()
# out_lst = []
#
# for i in trigram_boi:
#     out_lst.append(i[0])  # adds first item of key to the list
#     out_lst.append(i[1])  # adds second item of key to the list
#     out_lst.append(random.choice(trigram_boi[i]))  # adds random value to the list from that key


def seed_next_one(seed):  # returns a third item given a dictionary key
    product_list = [random.choice(trigram_boi[seed])]  # list, finds third item using key/seed

    new_key = (seed[1], product_list[0])  # tuple, made from second part of key/seed and the new third item

    if new_key not in trigram_boi:
        return product_list[:6]

    product_list += seed_next_one(new_key)

    return product_list[:6]


# def next_ones(new):
#     product_list = [random.choice(trigram_boi[new])]
#     return product_list


def random_seed_pls(dicc):  # returns a random key (type tuple) in the dictionary!
    this_list = []
    that_list = []
    for j in dicc:
        that_list.append(j)
    this_list.append(random.choice(that_list))
    return this_list[0]


shit_table = []

a = random_seed_pls(trigram_boi)

shit_table += [a[0]]

shit_table += [a[1]]

shit_table += seed_next_one(a)

print(shit_table)

# print(seed_next_one(random_seed_pls(trigram_boi)))

# print(seed_next_one(('wish', 'I')))

# print('^ the first two items, chosen randomly, plus a following value that, if applicable is chosen randomly too')

# a = (seed_next_one(random_seed_pls(trigram_boi), trigram_boi))

# final_list = []
# final_list.append(random_seed_pls(trigram_boi))
# for k in range(len(trigram_boi)):
#
# print(final_list)


# print(next_ones(seed_next_one(random_seed_pls(trigram_boi), trigram_boi), trigram_boi))

# for i in range(len(out_lst)-2):
#     print(trigram_boi[out_lst[i+1], out_lst[i+2]])


    # out_lst.append(trigram_boi[out_lst[i]])
    # out_lst.append(trigram_boi[out_lst[i]])



    # uses 2nd n 3rd item in new list as key in trigram dict
    # so the next value can be added to the list

    # if out_lst[i:(i + 2)] in trigram_boi:  # the previous two
    #     out_lst.append(random.choice(trigram_boi[i]))
# print(out_lst)
# print('^randomized trigram, now a list')

# print('I wish I may I wish I might')
# print(build_trigrams(read_file()))

# print(random_seed_pls(trigram_boi))
# print('^hopefully a random key ("seed") from the trigram dictionary^')


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

