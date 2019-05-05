#!/usr/bin/env python3

# series 1

l1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(l1)

ask = [input('what fruit would you like to add to the list? ').capitalize()]
l1 += ask
print(l1)

ask_2 = int(input('what number item in the list would you like to display? '))
print(l1[ask_2 - 1])

ask_3 = [input('what fruit do you want to add to the beginning of the list? ').capitalize()]
l1 = ask_3 + l1
print(l1)

ask_4 = input('yet anther fruit ').capitalize()
l1.insert(0, ask_4)
print(l1)

for _ in l1:
    if 'P' in _[0]:
        print(_)
    elif 'p' in _[0]:
        print(_)


# series 2

l2 = l1

print(l2)
print()
l2.pop(-1)
print(l2)
print()
l2.remove(input('what item would you like to remove? ').capitalize())
print(l2)
print()

# series 3

l3 = ['Banana', 'Blueberries', 'Apples', 'Pears', 'Oranges', 'Peaches', 'Kiwi']
print(l3)


def fruit_pref(lizt):
    for i in lizt[:]:
        in1 = input('Do you like?' + i.lower() + '\n').lower()
        if in1 == 'no':
            lizt.remove(i)
        elif in1 == 'yes':
            continue
        else:
            print('please only enter "yes" or "no" \ntry again')
            fruit_pref(lizt[:])
            return lizt
    return lizt


print(fruit_pref(l3))

# series 4


def reverse_reverse(seq):  # from slicing.py
    new_seq = seq[::-1]
    return new_seq


l4 = []
for i in l1:
    l4.append(reverse_reverse(i))

print(l4)
