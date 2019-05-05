#!/usr/bin/env python3


def open_file(file_name):
    with open(file_name) as input_file:
        read_file = input_file.readlines()

        for line in read_file:
            print(line)

    return


open_file("students.txt")



# Split after the first ","