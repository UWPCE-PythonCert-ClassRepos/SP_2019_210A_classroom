#!/usr/bin/env python3
# https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/list_lab.html

def series_one():
    fruits = ["Apples", "Pears,", "Oranges", "Peaches"]
    print(fruits)

    add_fruit = input("Please add another fruit here: ")
    fruits.append(add_fruit)
    print(fruits)

    add_number = input("Please add a number: ")
    for number in fruits:
        fruits[0].append(add_number)

    print(fruits)


if __name__ == "__main__":

    series_one()