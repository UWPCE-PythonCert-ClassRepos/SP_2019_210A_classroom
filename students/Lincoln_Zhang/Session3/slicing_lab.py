#!/usr/bin/env python3

#
#Week 3 Homework 1
#Slicing Lab
#https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/slicing.html
#

test_string = "I am a string"
test_list = ["I","am","a","List"]
test_tuple = (2, 54, 13, 12, 5, 32)

def swap_head_tail(seq):
	new_seq = []
	new_seq = seq[-1:] + seq[1:-1] + seq[0:]
	return new_seq

def every_other(seq):
	return seq[::2]

def pop_4(seq):
	new_seq = seq[4:-4:2]
	return seq_1[::2]

def reverse(seq):
	return seq[::-1]

def the_third(seq):
	new_seq = seq[::-3]
	return new_seq[1::-1]



def check_seq(seq):
	# test_string = "I am a string"
	assert swap_head_tail(test_string) == "g am a strinI"
	assert every_other(test_string) == "Ia  tig"
	assert pop_4(test_string) == " t"
	assert reverse(test_string) == "gnirts a ma I"
	assert the_third(test_string) == "rg"

	# test_list = ["I","am","a","List"]
	assert swap_head_tail(test_list) == ""


	return print("all tests passed")


if __name__ == "__main__":
	print(test_string)
	print(check_seq(test_string))
	print(test_list)
	print(check_seq(test_list))
	print(test_tuple)
	print(check_seq(test_tuple))


#assert swap_head_tail() == 