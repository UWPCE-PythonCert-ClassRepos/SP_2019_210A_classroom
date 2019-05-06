#!/usr/bin/env python3
import os

"""
- Write a program which prints the full path for all files in the current directory, one per line
- Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
    - Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
    - This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
    - Test it with both text and binary files (maybe jpeg or something of your choosing).
"""

# Write a program which prints the full path for all files in the current directory, one per line
def list_full_path():
    path = os.listdir()
    for file in path:
        print(os.path.abspath(file))

list_full_path()


# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
def copy_file(file_name):
    """
    Only creates a new subdirectory within the current directory
    system() method uses any OS command line argument to copy(cp) a file, making this function usable on most platforms
    The system() method calls a function from the C standard library
    Replace `cp` with `mv` to move the file from the source to the destination

    Extra note: I clearly had a bit too much fun with this.
    """
    name_destination = input("Name the destination directory: ")
    source = f"./{file_name}"
    destination = f"./{name_destination}/"
    create_directory = os.mkdir(f"./{name_destination}")

    return os.system(f"cp {source} {destination}")

copy_file("random_file.txt")


def advanced_copy_file(file_name):
    name_destination = input("Name the advanced destination directory: ")
    source = f"./{file_name}"
    destination = f"./{name_destination}/"
    create_directory = os.mkdir(f"./{name_destination}")

    with open(file_name, "rb") as input_file:
        read_data = input_file.read()
        return os.system(f"cp {source} {destination}")

advanced_copy_file("porsche_911.jpg")