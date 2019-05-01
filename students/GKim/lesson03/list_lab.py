
"""
Step 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.

Step 2
Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

Step 3
Again, using the list from series 1:

Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list 
(making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values 
(a while loop is good here)
Display the list.

Step 4
Once more, using the list from series 1:

Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy.

"""
inv = ["Apple","Pears","Oranges","Peaches"]
e_list = []

def print_list(lst):
    for x in lst:
        print(x)
    return

def question():
    response = input("\nPlease enter another fruit: \n")
    return response

def letter_p(lst):
    print("\nHere are fruits that start with the letter 'P'\n")
    for x in lst:
        if "P" in x:
            print("'P' fruits: ", x)
            return

def reverse_word(word):
    return word[::-1]

def series_1():
    print_list(inv)
    print()
    response = question()
    inv.append(response)
    print_list(inv)

    num = int(input("\nPlease give me a number (1-5): "))
    print("{}: {}".format(num,inv[num-1]))

    response = question()
    e_list.append(response)
    new_inv = e_list + inv # concatenating two list together
    print_list(new_inv)

    response = question()
    new_inv.insert(0,response)
    print_list(new_inv)

    letter_p(new_inv) # show fruits with the letter "P"

def series_2():   
    print_list(inv)
    inv.pop(-1) # removing the last item on the list.
    print("\nNew list with last item removed\n")
    print_list(inv)
    while True:
        delete_f = input("What fruit would you like to delete? \n")
        for x in inv:
            if delete_f in x:
                inv.remove(delete_f)
                print(inv)
                return False
        
        print("\nPlease check spelling and make sure its in the list\n")

def series_3():
    print_list(inv)
    
    new_inv = []
    while True:
        x = 0
        for x in range(len(inv)-1, -1, -1):
            like_fruit = input("Do you like {}'s? ".format(inv[x]))
            if like_fruit.lower() == "y" or like_fruit.lower() == "yes":
                new_inv.append(inv[x].lower())
            elif like_fruit.lower() == "n" or like_fruit.lower() == "no":
                inv.remove(inv[x])
               
            else:
                print("Please answer Yes or No (y/n)")
        print_list(new_inv)
        return False
        
def series_4():


    # rev_inv = [[x[::-1]] for x in inv][::-1]
    inv.pop(-1)
    print("original list: ", inv)
    reverseWords = [reverse_word(word) for word in inv]
    print("reversed letters list: ", reverseWords)

def main():
    # series_1()
    # series_2()
    # series_3()
    series_4()
    
    



if __name__ == "__main__": main()