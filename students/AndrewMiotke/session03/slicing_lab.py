#!/usr/bin/env python3
# https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/slicing.html

# Global namespace variables to slice

string_one = "here is the first string"
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
thirds_strings = "split this string"

def slicing_one(seg):
    return seg

def first_to_last():
    first = numbers[:1]
    second = numbers[0]
    third = numbers[-1:]

    return third + second + first

first_to_last()


def slicing_two():
    new_string_one = thirds_strings[0:5]
    new_string_two = thirds_strings[7:10]
    new_string_three = thirds_strings[12:18]
    final_string = new_string_three + new_string_one + new_string_two
    print(f"Slicing Two: {final_string}")

slicing_two()


if __name__ == "__main__":
    print(slicing_one(string_one[1:-1]))
    print(slicing_one(numbers[::2]))
    print(slicing_one(numbers[4:-4:2]))
    print(slicing_one(string_one[::-1]))

    assert slicing_one(numbers) == (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)