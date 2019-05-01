#! /usr/bin/env python3
"""
Paths and File Processing
Author : Joe Nunnelley
"""
import os

def list_cwd():
    """
    List the contents of the current folder

    Write a program which prints the full path for all files
    in the current directory, one per line
    """
    cwd = os.getcwd()
    for filename in os.listdir():
        print("- {}/{}".format(cwd, filename))

def copy_file(source_file, destination_path, binary=False):
    """
    Copy text or binary files from a source location to a destination location

    Write a program which copies a file from a source, to a
    destination (without using shutil, or the OS copy command).
        Advanced: make it work for any size file: i.e. don’t read
        the entire contents of the file into memory at once.
        This should work for any kind of file, so you need to open
        the files in binary mode: open(filename, 'rb') (or 'wb' for writing).
        Note that for binary files, you can’t use readline() – lines don’t
        have any meaning for binary files.
        Test it with both text and binary files (maybe jpeg or something of
        your choosing).
    """
    dest = "{}/{}".format(destination_path, source_file)
    read_mode = 'rb' if binary else 'r'
    write_mode = 'wb' if binary else 'w'
    source_file_path = '{}/{}'.format(os.getcwd(), source_file)
    print("Copying {} to {}".format(source_file, destination_path))

    with open(source_file_path, read_mode) as infile, open(dest, write_mode) as outfile:
        outfile.write(infile.read())


def process_students(stuents_file):
    """
    File reading and parsing

    Download this text file:
        students.txt

    In it, you will find a list of names and what programming languages
    they have used in the past. This may be similar to a list generated
    at the beginning of this class.

    Write a little script that reads that file, and generates a list of
    all the languages that have been used.

    What might be the best data structure to use to keep track of bunch
    of values without duplication?
    The file format:

        The first line of the file is:

        Name: Nickname, languages

    And each line looks something like this:

        Jagger, Michael: Mick, shell, python

    So a colon after the name, then the nickname, and then one or more
    languages.

    However, like real data files, the file is NOT well-formed. Only
    some lines have nicknames, and other small differences, so you will
    need to write some code to make sure you get it all correct.

    Extra challenge: keep track of how many students specified each language.
    """
    lines = []
    with open(text_file) as infile:
        lines = infile.readlines()

    for line in lines[1::]:
        name, rest = line.split(':', 2)
        rest = rest.replace(" ",',').replace('\n', '')
        rest_array = rest.split(',')
        print(rest_array)
        nicknames = []
        languages = []

        for index, item in enumerate(rest_array):
            print(item)
            item = item.lstrip()
            print(">> {}".format(item))
            if str.isupper(item[0:1]) and len(item) > 0:
                print("\tName: {}".format(item))
                nicknames.append(item)
                rest_array.pop(index)
            elif str.islower and len(item) > 0:
                print("\tLanguage: {}".format(item))
                languages.append(item)
            else:
                print('Didnt process {}'.format(item))

        print(f'name: {name:20} nickname: {" ".join(nicknames):15}\tlanguages: {" ".join(languages)}')




if __name__ == "__main__":
    #list_cwd()
    text_file = 'students.txt'
    binary_file = 'magic.jpg'
    #destination_path = input('Copy to :> ')
    #copy_file(text_file, destination_path)
    #copy_file(binary_file, destination_path, True)
    process_students(text_file)

