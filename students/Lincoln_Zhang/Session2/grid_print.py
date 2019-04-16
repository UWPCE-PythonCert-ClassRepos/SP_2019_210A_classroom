#
#Session 2 Class excercise
#print grid like this
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +

def print_plus():
	print ("+",end="")

def print_minus():
	print(" - - - - ",end="")

def print_space():
	print("         ",end="")

def print_pipe():
	print("|",end="")

def print_newline():
	print("\n")

def grid_print(r):
	for r in range(r):
		if r%5 == 0:
			print_plus()
			print_minus()
			print_plus()
			print_minus()
			print_plus()
			print_newline()
		else:
			print_pipe()
			print_space()
			print_pipe()
			print_space()
			print_pipe()
			print_newline()

grid_print(11)

#if __name__ == "__main__":
#	print("module is imported")
#	grid_print(11)

