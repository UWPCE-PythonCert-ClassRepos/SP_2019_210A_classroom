#!/usr/bin/env python3

raw_data = {'name':'Chris','city':'Seattle','cake':'Chocolate'}

def dict_1():
	print(raw_data)
	raw_data.pop('cake')
	print(raw_data)
	raw_data.update({'fruit':'mongo'})
	print(raw_data)
	print(raw_data.keys())
	print(raw_data.values())

	k = 'cake'
	v = 'mongo'

	if not k in raw_data.keys():
		return print("cake is not the key")
	if v in raw_data.values():
		return print("mongo is the value")


def dict_2():
	for i in raw_data:
		ts = raw_data[i]
		raw_data[i] = ts.count('t')
	return raw_data

def set_1():
	s2 = []
	s3 = []
	s4 = []
	for n in range(21):
		if not n%2:
			s2.append(n)
		if not n%3:
			s3.append(n)
		if not n%4:
			s4.append(n)
	s2 = set(s2)
	s3 = set(s3)
	s4 = set(s4)
	print(s2,s3,s4)
	print("Is s3 subset of s2 ? {}".format(s3.issubset(s2)))
	print("Is s4 subset of s2 ? {}".format(s4.issubset(s2)))





if __name__ == '__main__':
	dict_1()
	print(dict_2())
	set_1()