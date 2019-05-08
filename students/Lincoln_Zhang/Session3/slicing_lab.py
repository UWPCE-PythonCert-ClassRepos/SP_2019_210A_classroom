#!/usr/bin/env python3

#
#Week 3 Homework 1
#Slicing Lab
#https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/slicing.html
#

test_string = "I am a string"
test_list = ["I","am","a","List","add","some","strings","to","prolong","the","length","of","it"]
test_tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)

def swap_head_tail(seq):
    new_seq = []
    new_seq = seq[-1:] + seq[1:-1] + seq[0:]
    return new_seq[:len(seq)]

def every_other(seq):
    return seq[::2]

def pop_4(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]

def the_third(seq):
    new_seq = seq[::-3]
    return (new_seq[0:] + new_seq[::-1][1::])[:len(new_seq)]



def check_seq():
    # test_string = "I am a string"
    assert swap_head_tail(test_string) == 'g am a strinI'
    assert every_other(test_string) == 'Ia  tig'
    assert pop_4(test_string) == '  t'
    assert reverse(test_string) == 'gnirts a ma I'
    assert the_third(test_string) == 'gr mI'

    # test_list = ["I","am","a","List","add","some","strings","to","prolong","the","length","of","it"]
    assert swap_head_tail(test_list) == ['it', 'am', 'a', 'List', 'add', 'some', 'strings', 'to', 'prolong', 'the', 'length', 'of', 'I']
    assert every_other(test_list) == ['I', 'a', 'add', 'strings', 'prolong', 'length', 'it']
    assert pop_4(test_list) == ['add', 'strings', 'prolong']
    assert reverse(test_list) == ['it', 'of', 'length', 'the', 'prolong', 'to', 'strings', 'some', 'add', 'List', 'a', 'am', 'I']
    assert the_third(test_list) == ['it', 'the', 'strings', 'List', 'I']

    # test_tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)
    assert swap_head_tail(test_tuple) == (22, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 1)
    assert every_other(test_tuple) == (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21)
    assert pop_4(test_tuple) == (5, 7, 9, 11, 13, 15, 17)
    assert reverse(test_tuple) == (22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    assert the_third(test_tuple) == (22, 19, 16, 13, 10, 7, 4, 1)

    return print("all tests passed")


if __name__ == "__main__":
    check_seq()

