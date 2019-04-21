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

def horizontal_line(boxsize):
	return "- " * boxsize + "+ "

def vertical_line(boxsize):
	return "  " * boxsize + "| " 

# def grid_print_1(boxsize, gridsize):
# 	r = horizontal_line(boxsize)
# 	c = vertical_line(boxsize)
# 	for _ in range(gridsize+1):
# 		if _%boxsize == 0:
# 			print ("+ " + r*gridsize)
# 		else:
# 			for _ in range(boxsize):
# 				print ("| " + c*gridsize)

def grid_print_2(boxsize, gridsize):
	r = horizontal_line(boxsize)
	c = vertical_line(boxsize)
	for _ in range((boxsize+1)*gridsize+1):
		if _%(boxsize+1) == 0:
			print ("+ " + r*gridsize)
		else:
			print ("| " + c*gridsize)

# print("grid_print_1 output: ")
# grid_print_1(boxsize, gridsize)

print("grid_print_2 output: ")
grid_print_2(boxsize, gridsize)

print("grid_print_2 is the solution to this assignment")	

# if __name__ == "__main__":
# 	print("module is imported")
# 	grid_print(11)