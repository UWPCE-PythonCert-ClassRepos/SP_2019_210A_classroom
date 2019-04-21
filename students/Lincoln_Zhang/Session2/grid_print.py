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
n = int(input("Please input a positive integer: ")) + 1

def horizontal_line(boxsize):
	return "- " * boxsize + "+ "

def vertical_line(boxsize):
	return "  " * boxsize + "| " 

#a scale function for a 4X4 grid
def grid_print_1(n):
	if not (n-1)%4:
		r = "- "*int((n-1)/2) + "+ " + "- "*int((n-1)/2)
		c = "  "*int((n-1)/2) + "| " + "  "*int((n-1)/2)

		for _ in range(n+2):
			if _%int((n-1)/2+1) == 0:
				print ("+ " + r + "+")
			else:
				print ("| " + c + "|")
	else:
		n = input("Please input an integer n modulo 4 is 0: ")


def grid_print_2(boxsize, gridsize):
	r = horizontal_line(boxsize)
	c = vertical_line(boxsize)
	for _ in range((boxsize+1)*gridsize+1):
		if _%(boxsize+1) == 0:
			print ("+ " + r*gridsize)
		else:
			print ("| " + c*gridsize)

print("grid_print_1 output: ")
grid_print_1(n)

print("grid_print_2 output: ")
grid_print_2(boxsize, gridsize)

#print("grid_print_2 is the solution to this assignment")	

# if __name__ == "__main__":
# 	print("module is imported")
# 	grid_print(11)