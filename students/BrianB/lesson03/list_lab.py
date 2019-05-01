#!/usr/bin/env python3

import sys  # imports go at the top of the file

fruits = ["Apples", "Pears", "Oranges", "Peaches"]

prompt = "\n".join(("Welcome to the fruit stand!",
                    "Please choose from below options:",
                    "1 - View all fruits",
                    "2 - Add a fruit",
                    "3 - View a specific fruit",
                    "4 - Remove a fruit",
                    "5 - Mystery Display",
                    "6 - Execute Fruit List Reversal",
                    "7 - Exit",
                    ">>> "))


def view_fruits():
    item = input("Would you like to display fruits that\n"
    "only begin with the letter 'P'? Enter 'Yes'.\n"
    "Otherwise Enter 'No' to view ALL Fruits.")
    if item.lower() in ("n", "no"):
        print("\n".join(fruits))
    elif item.lower() in ("y", "yes"):
        for fruit in fruits:
            if fruit[0].lower() == "p":
                print(fruit)


def view_a_fruit():
    item = input("Choose a fruit by its Pythonic number: ")
    item = int(item)
    if -1 < item < len(fruits):
        print(item, fruits[item-1])
    else:
        return prompt


def add_fruit():
    new_fruit = input("Name of the fruit to add?").title()
    new_location = input("Enter '1' to add fruit to the beginning\
 of the list.\n" "Enter '2' to add fruit to the end of the list").title()
    if new_location == "2":
            fruits.append(new_fruit)
    else:
        fruits.insert(0, new_fruit)


def remove_fruit():
    purge_fruit = input("Name of the fruit to remove?").title()
    if purge_fruit not in fruits:
        print("This fruit does not exist!")
    else:
        fruits.remove(purge_fruit)


def mystery_display():
    fruit = 0
    while fruit < len(fruits):
        item = input("Do you like {}? (y/n): ".format(fruits[fruit].lower()))
        print(fruit)
        while True:
            if item.lower() == "y":
                fruit = fruit+1
                break
            if item.lower() == "n":
                print('Removing {}'.format(fruits[fruit].lower()))
                fruits.remove(fruits[fruit])
                print(fruit)
                print(len(fruits))
                break
            else:
                item = input("Please answer 'yes' or 'no' only.\n")

    print(fruits)


def reverse_fruit():
    for fruit in fruits:
        transposed_fruits = fruit[::-1]
        print(transposed_fruits)

    del fruits[-1]
    print(fruits)


def exit_program():
    print("Bye!")
    # exit the interactive script
    sys.exit()


def main():
    while True:
        # continuously collect user selection
        response = input(prompt)
        # now redirect to feature functions based on the user selection
        if response == "1":
            view_fruits()
        elif response == "2":
            add_fruit()
        elif response == "3":
            view_a_fruit()
        elif response == "4":
            remove_fruit()
        elif response == "5":
            mystery_display()
        elif response == "6":
            reverse_fruit()
        elif response.lower == "7" or "Exit":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    # don't forget this block to guard against your code
    # running automatically if this module is imported
    main()
