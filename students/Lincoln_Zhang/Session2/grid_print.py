#!/usr/bin/env python3

#Session 2 Class excercise
#print grid like this

print("Please make a script generating grid like this.")

print("""
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
""")

boxsize = int(input("Please input box size: "))
gridsize = int(input("Please input grid size: "))
n = int(input("Please input a positive integer: ")) 

def horizontal_line(boxsize):
	return "- " * boxsize + "+ "

def vertical_line(boxsize):
	return "  " * boxsize + "| " 


def grid_print_1(n):
	r = "- "*n + "+ " + "- "*n
	c = "  "*n + "| " + "  "*n

	for _ in range(n*2+2):
		if not _%(n+1):
			print ("+ " + r + "+")
		else:
			print ("| " + c + "|")
	print ("+ " + r + "+")


def grid_print_2(boxsize, gridsize):
	r = horizontal_line(boxsize)
	c = vertical_line(boxsize)
	for _ in range((boxsize+1)*gridsize+1):
		if not _%(boxsize+1):
			print ("+ " + r*gridsize)
		else:
			print ("| " + c*gridsize)

print("grid_print_1 output: ")
grid_print_1(n)

print("grid_print_2 output: ")
grid_print_2(boxsize, gridsize)
	

# if __name__ == "__main__":
# 	print("module is imported")
# 	grid_print(11)