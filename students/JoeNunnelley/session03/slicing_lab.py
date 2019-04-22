#! /usr/bin/env python3

def exchange_first_last(seq):
    if type(seq) == str:
        return seq[-1] + seq[1:-1] + seq[0]
    elif type(seq) == tuple:
        exchanged = (seq[-1::] + seq[1:-1] + seq[0:1])
        return exchanged
    elif type(seq) == list:
        exchanged = []
        exchanged.append(seq[-1])
        exchanged.extend(seq[1:-1])
        exchanged.append(seq[0])
        return exchanged
    else:
        print('Unrecognized seqence')
        return seq

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [2, 4, 5, 6, 7, 8]

print('Before: {}'.format(a_string))
print('After: {}'.format(exchange_first_last(a_string)))
print('Before: {}'.format(a_tuple))
print('After: {}'.format(exchange_first_last(a_tuple)))
print('Before: {}'.format(a_list))
print('After: {}'.format(exchange_first_last(a_list)))

print('Running tests...')
assert(exchange_first_last(a_string)) == 'ghis is a strint'
assert(exchange_first_last(a_tuple)) == (32, 54, 13, 12, 5, 2)
assert(exchange_first_last(a_tuple)) == (32, 54, 13, 12, 5, 2)
print('No asserts. Functionality correct')
