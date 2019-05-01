#!/usr/bin/env python3



num_1 = int(input("Please input the 1st number: "))
num_2 = int(input("Please input the 2nd number: "))

def fibonacci(n):

	l = [num_1,num_2]
	if num_1 == 0 and num_2 ==1:
		print("A Fibonacci series is generated.")
	elif num_1 == 2 and num_2 == 1:
		print("A Lucas series is generated.")
	else:
		print("A series is generated.")
	while len(l) <= n:
		new_num = l[-1] + l[-2]
		l.append(new_num)
		# print(l)
	return l[-1]

print(fibonacci(5))
