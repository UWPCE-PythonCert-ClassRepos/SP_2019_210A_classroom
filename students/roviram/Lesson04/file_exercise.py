#------------------- Script Details---------------------#
# Week 4 Homework: File Exercise
# Miguel Rovira-Gonzalez, 5/5/19, created File Exercise
#-------------------------------------------------------#
import pathlib
import os
import re
import string
import numpy as np
from collections import Counter, OrderedDict

"""
Write a program which prints the full path for all files in the current directory, one per line. Use either the os module or pathlib.
Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command (you are essentially writing a simple version of the OS copy command)).
    This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
    Test it with both text and binary files (maybe a jpeg or something of your choosing).
    Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
    This should only be a few lines of code :-)
"""
# Data
source = r"C:\Users\roviram\Python_210\SP_2019_210A_classroom\students\roviram\Lesson03\test.rb"
destination = "new_junk.rb"

def path():
    """
    Writes a program which prints the full path for all files in the current directory, one per line using pathlib module.
    """
    file_path = pathlib.Path('./')
    file_path.is_dir()
    file_path.absolute()
    for file in file_path.iterdir():
        print(file)

def copy_file(source, destination):
    print("Source File:", source, "\nDestination File:", destination)
    with open(source, 'rb') as infile, open("Copy of " + destination, 'wb') as outfile:
        outfile.write(infile.read())

def read_file(file_name):
    with open(file_name, "r") as obj_file:
        student_lang_lst = []
        for line in obj_file:
            student_name = line.strip().split(":")[0]
            student_nick_name = ''
            second_half = line.replace(' ', "").strip().split(":")[1].split(",")
            for part in second_half:
                if part:
                    if not part[0].islower():
                        student_nick_name = part
                    else:
                        student_lang_lst.append(part)
        final = set(student_lang_lst)
        for index, lang in enumerate(final):
            print(str(index + 1) + ".", lang)

if __name__ == '__main__':
    read_file("students.txt")

