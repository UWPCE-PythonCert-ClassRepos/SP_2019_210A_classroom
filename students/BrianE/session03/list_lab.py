#!/usr/env python3

"""
    list_lab.py
"""


def display_fruits(fruits):
    """
    Print fruit list contents to terminal
    :param fruits: list of fruits
    :return: None
    """

    print("Current fruit: {}".format(fruits))


def delete_fruits(fruits):
    """
    Delete fruit item from list
    :param fruits: string
    :return: None
    """

    print(fruits)
    fruit_to_delete = input("Enter a fruit to delete: \n\n >>>")
    try:
        index = fruits.index(fruit_to_delete)
        del fruits[index]
    except ValueError as e:
        print(e)


def cleanup_list(fruits):
    """
    Remove fruits from list if user does not like
    :param fruits: list of fruits
    :return: None
    """

    deleted_fruits = []

    for i in range(0, len(fruits)):
        while True:
            answer = input(f"Do you like {fruits[i]}?").lower().strip()
            if answer == 'yes':
                break
            elif answer == 'no':
                deleted_fruits.append(fruits[i])
                break
            else:
                print(f"Please choose from the following: yes|no")
                continue

    for fruit in deleted_fruits:
        fruits.remove(fruit)


def main():
    """
    Series 1
    * Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    * Display the list (plain old print() is fine…).
    * Ask the user for another fruit and add it to the end of the list.
    * Display the list.
    * Ask the user for a number and display the number back to the user and the fruit corresponding to that number
      (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    * Add another fruit to the beginning of the list using “+” and display the list.
    * Add another fruit to the beginning of the list using insert() and display the list.
    * Display all the fruits that begin with “P”, using a for loop.
    """

    fruits = ["Apples", "Pears", "Oranges", "Peaches"]

    display_fruits(fruits)
    fruits.append(input("Which fruit would you like to add?\n\n  >>>"))
    display_fruits(fruits)

    number = int(input("Please enter a number: \n\n  >>>"))
    print(f"You entered {number}, which corresponds with {fruits[number - 1]}")
    fruits = list([input("Enter another fruit: \n\n  >>>")]) + fruits
    display_fruits(fruits)

    fruits.insert(0, input("Enter another fruit: \n\n  >>>"))
    print("Fruits in list with 'P' in name:")
    for fruit in fruits:
        if "p" in fruit[0].lower():
            print(fruit)

    """
    Series 2
    Using the list created in series 1 above:

    * Display the list.
    * Remove the last fruit from the list.
    * Display the list.
    * Ask the user for a fruit to delete, find it and delete it.
    * (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
    """

    display_fruits(fruits)
    fruits.pop()
    display_fruits(fruits)

    delete_fruits(fruits)
    display_fruits(fruits)

    """
    Series 3
    Again, using the list from series 1:

    * Ask the user for input displaying a line like “Do you like apples?” for each fruit
      in the list (making the fruit all lowercase).
    * For each “no”, delete that fruit from the list.
    * For any answer that is not “yes” or “no”, prompt the user to answer with one of those
      two values (a while loop is good here)
    * Display the list.
    """
    cleanup_list(fruits)
    display_fruits(fruits)

    """
    Series 4
    Once more, using the list from series 1:

    * Make a new list with the contents of the original, but with all the letters in each item reversed.
    * Delete the last item of the original list. Display the original list and the copy.
    """

    reversed_fruits = [fruit[::-1] for fruit in fruits]
    fruits.pop()
    print(f"Original list: {fruits}")
    print(f"Reversed list: {reversed_fruits}")


if __name__ == '__main__':
    main()

