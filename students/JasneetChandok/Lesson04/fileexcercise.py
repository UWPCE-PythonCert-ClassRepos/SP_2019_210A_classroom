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

# File reading and parsing
distinct_langs = set()
path2 = path / "students.txt" # directing the path to your student directory
with open(path2) as stdfile:
    stdfile.readline()
    for rows in stdfile:
        langs = rows.split(':')[1]  
        langs = langs.replace(',', ' ')
        langs = langs.replace('and', ' ')
        langs = langs.split()
        for lang in langs:
            if lang:
                distinct_langs.add(lang)

for lang in distinct_langs:
    print(lang)



