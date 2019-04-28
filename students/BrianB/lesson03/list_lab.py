#!/usr/bin/env python3

import sys  # imports go at the top of the file
import random  # imports a random module for the myster display function

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
    item = input("Would you like to display fruits that only begin\
 with the letter 'P'? Enter 'Yes'.  Otherwise Enter 'No' to view ALL Fruits.")
    if item.lower() == "No" or "N":
        print("\n".join(fruits))
    elif item.lower() == "Yes" or "Y":
        for fruit in fruits:
            if fruit[0].lower() == "P":
                fruits.remove(fruit)
            print(fruits)


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
    for fruit in fruits:
        item_3 = input("Do you like {}? (y/n): ".format(fruit.lower()))

        while item_3 != "y" or item_3 != "n":
            if item_3.lower() == "y":
                break
            if item_3.lower() == "n":
                fruits.remove(fruit)
                print('Removing {}'.format(fruit))
                break
            else:
                print("Please answer 'yes' or 'no' only.\n")

                item_3 = input(
                    "Do you like {}? (yes/no): ".format(fruit.lower()))

    print(fruits)


def reverse_fruit():
    fruits_4 = fruits
    new_fruits_4 = list()

    for fruit in fruits_4:
        reversed_fruit = fruit[::-1]
        new_fruits_4.append(reversed_fruit)

    print(new_fruits_4)

    del fruits_4[-1]
    print(fruits_4)


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
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
