"""
this program uses dictionaries for menus
from Lesson 4, video 3 Python's missing switch statement
"""

def menu_selection(prompt, dispatch_dict):
    while True: #this loops forever, until quit is selected
        response = input(prompt)
        response = response[:1].lower()
        if dispatch_dict.get(response, unknown)() == "exit menu":
            break

def fun1():
    print("You selected the first option.")

def fun2():
    print("You selected the second option.")

def fun3():
    print("You selected the third option.")

def fun4():
	print("You selected the fourth option.")

def sum_menu():
    menu_selection(sub_prompt, sub_dispatch)

def quit():
    print("Quitting the menu now.")
    return "exit menu"

def unknown():
    print("that was not a valid response")
    return None

main_prompt = ("You are in the main menu now\n"
			   "What do you want to do?\n"
			   "Type 1, 2, 3, 4 or 5 to get a sub-menu\n"
			   "or q to exit >>")


main_dispatch = {"1" : fun1,
                 "2" : fun2,
                 "3" : fun3,
                 "4" : fun4,
                 "5" : sum_menu,
                 "q" : quit
	             }


sub_prompt = ("\nYou are in a sub-menu now\n"
			  "What do you want to do?\n"
			  "Type 1, 2, 3, or 4, or q to exit >>"
			  )

sub_dispatch = {"1" : fun1,
				"2" : fun2,
				"3" : fun3,
				"4" : fun4,
				"q" : quit
				}

if __name__ == "__main__":
    #try a couple menu selections
    menu_selection(main_prompt, main_dispatch)





