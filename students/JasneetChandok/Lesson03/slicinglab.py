#!/usr/bin/env python3.6

'''Module 3 - Slicing Lab Excercise'''


def first_last_exchange(seq):
	'''First and last item exchanged'''
	new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
	return new_sequence


def every_other(seq):
	'''Every other item removed'''
	new_sequence = seq[::2]
	return new_sequence


def first4_last4_eveyother(seq):
	'''First 4 and the last 4 items removed, and then every other item in the remaining sequence'''
	new_sequence = seq[4:-4:2]
	return new_sequence


def elements_reversed(seq):
	'''elements reversed (just with slicing)'''
	new_sequence = seq[::-1]
	return new_sequence


def first_last_middle_thrid(seq):
	'''Last third, then first third, then the middle third in the new order'''
	new_sequence = seq[-3:] + seq[:3] + seq[(len(seq)//3):(len(seq)//3)*2]
	return new_sequence


def main():

	a_string = "this is a string"
	a_tuple = (2, 54, 13, 12, 5, 32)
	a_list = [2, 'age', 13, 12, 5, 'dog']
	a_longtuple = (2,54,13,12,5,32,24,45,23,223,232,67,789,87)

	# Test - first and last item exchanged
	assert first_last_exchange(a_string) == "ghis is a strint"
	assert first_last_exchange(a_tuple) == (32, 54, 13, 12, 5, 2)
	assert first_last_exchange(a_list) == ['dog', 'age', 13, 12, 5, 2]

	#Test - every other item removed
	assert every_other(a_string) == "ti sasrn"
	assert every_other(a_tuple) == (2,13,5)
	assert every_other(a_list) ==[2,13,5]

	#Test - first 4 and the last 4 items removed, and then every other item in the remaining sequence
	assert first4_last4_eveyother(a_string) == " sas" 
	assert first4_last4_eveyother(a_longtuple) == (5,24,23)
	assert first4_last4_eveyother(a_tuple) == ()
	assert first4_last4_eveyother(a_list) == []

	#Test - elements reversed (just with slicing)
	assert elements_reversed(a_string) == "gnirts a si siht"
	assert elements_reversed(a_tuple) ==(32, 5, 12, 13, 54, 2)
	assert elements_reversed(a_list) ==['dog', 5, 12, 13, 'age', 2]

	#Test - last third, then first third, then the middle third in the new order
	assert first_last_middle_thrid(a_string) == "ingthiis a "
	assert first_last_middle_thrid(a_longtuple) == (67,789,87,2,54,13,5,32,24,45)

	print("All Assertions Passed")


if __name__ == '__main__':
	main()