#!/usr/bin/env python3.6

'''Lesson 4: File Excercise'''

import os
import glob
import pathlib

# Path and File Processing

# Part 1
folder_path = os.getcwd()
list_of_file = glob.glob(os.path.join(folder_path, '*.py'))

for file_name in list_of_file:
    print(file_name)


# Part 2
path = pathlib.Path.cwd()
sourcefile_path = 'C:\\Users\\jchando1\\OneDrive - T-Mobile USA\\Programming in Python\\SP_2019_210A_classroom\\students\\JasneetChandok\\Readme.txt'
outfile_path = path / "outfile.txt"


with open(sourcefile_path, 'rb') as infile, open(outfile_path, 'wb') as outfile:
    outfile.write(infile.read())
    print("File was copied to the location shared")

print('\n')
print('\n')
print('\n')

# File reading and parsing

path2 = path / "students.txt"
with open(path2) as stdfile:
    for rows in stdfile:
        rows = rows.strip()
         = rows.split(":")
        print(extract1)

