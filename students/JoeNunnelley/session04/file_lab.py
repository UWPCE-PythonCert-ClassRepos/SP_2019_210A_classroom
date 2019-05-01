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
    print("\nList of files in: {}\n".format(os.getcwd()))
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
    print('\nCopy File\n')
    dest = "{}/{}".format(destination_path, source_file)
    read_mode = 'rb' if binary else 'r'
    write_mode = 'wb' if binary else 'w'
    source_file_path = '{}/{}'.format(os.getcwd(), source_file)
    print("Copying {} to {}".format(source_file, destination_path))

    with open(source_file_path, read_mode) as infile, open(dest, write_mode) as outfile:
        outfile.write(infile.read())


def process_students(text_file):
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
    print('\nProcess Student File\n')
    lines = []
    with open(text_file) as infile:
        lines = infile.readlines()

    language_sum = {}
    for line in lines[1::]:
        name, rest = line.split(':', 2)
        rest_array = list(filter(None,
                                 rest
                                 .replace(" ", ",")
                                 .replace('\n', '')
                                 .split(',')))

        nicknames = []
        languages = []

        for item in rest_array:
            item = item.strip()
            if str.isupper(item[0:1]):
                nicknames.append(item)
            else:
                languages.append(item)

                if item not in language_sum.keys():
                    language_sum[item] = 1
                else:
                    language_sum[item] = language_sum[item] + 1

        print(f'name: {name:20} '
              f'nickname: {" ".join(nicknames):15}\t'
              f'languages: {" ".join(languages)}')

    print("\n{:15} : {:>10}\n{}".format('Language', 'Students', '-' * 28))

    for key, value in language_sum.items():
        print("{:15} : {:>10}".format(key, value))


if __name__ == "__main__":
    TEXT_FILE = 'students.txt'
    BINARY_FILE = 'magic.jpg'

    list_cwd()
    DESTINATION_PATH = input('Copy to :> ')
    copy_file(TEXT_FILE, DESTINATION_PATH)
    copy_file(BINARY_FILE, DESTINATION_PATH, True)
    process_students(TEXT_FILE)
