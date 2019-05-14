#!/usr/bin/env python3

# TODO:
#  - create two lists
#     - list one: person's name
#     - list two: language
# - zip the two lists together


def open_file(file_name):
    languages = []
    people = []

    with open(file_name, "r") as input_file:
        read_file = input_file.readlines()

        for line in read_file:
            n = 3
            names = line.split(":")
            language = line.split(",")
            ":".join(names[:n]), ":".join(names[n:])
            people.append(names[0:-1])
            languages.append(language[1:])

        for p in people:
            print(p)

        for l in languages:
            print(l)

    return


open_file("students.txt")