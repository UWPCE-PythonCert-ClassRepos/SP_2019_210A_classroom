#!/usr/bin/env python3
def exchange_first_last(seq):
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return a_new_sequence

def exchange_first_last_remove_else(seq):
    a_new_sequence = seq[-1:] + seq[:1]
    return a_new_sequence

def remove_first4_last4(seq):
    a_new_sequence = seq[4:-4]
    return a_new_sequence

def reverse(seq):
    a_new_sequence = seq[::-1]
    return a_new_sequence

def thirds(seq):
    a_new_sequence = seq[2 * len(seq)//3:] + seq[:len(seq)//3] + seq[len(seq)//3:2*len(seq)//3]
    return a_new_sequence

def tester():
    a_string =  "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last_remove_else(a_string) == "gt"
    assert exchange_first_last_remove_else(a_tuple) == (32, 2)
    assert remove_first4_last4(a_string) == ' is a st'
    assert remove_first4_last4(a_tuple) == ()
    assert reverse(a_string) == 'gnirts a si siht'
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert thirds(a_string) == 'stringthis is a ', thirds(a_string)
    assert thirds(a_tuple) == (5, 32, 2, 54, 13, 12)

if __name__ == '__main__':
    tester()
