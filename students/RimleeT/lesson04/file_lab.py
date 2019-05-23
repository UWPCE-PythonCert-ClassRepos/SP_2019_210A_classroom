"""Paths and File Processing"""
"""Write a program which prints the full path for all files in the current directory, one per line. Use either the os module or pathlib."""
import os
from os import listdir
from os.path import join
for f in listdir(os.getcwd()):
    onlyfiles = join(os.getcwd(), f)
    print(onlyfiles)

"""Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command (you are essentially writing a simple version of the OS copy command)).
This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
Test it with both text and binary files (maybe a jpeg or something of your choosing).
Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
This should only be a few lines of code :-)"""
with open('D://Me.jpg','rb') as rf:
    with open('D://Me_copy.jpg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

"""File reading and parsing
Download this text file:
students.txt
In it, you will find a list of names and what programming languages they have used in the past. This may be similar to a list generated at the beginning of this class.
Write a little script that reads that file and generates a list of all the languages that have been used.
What might be the best data structure to use to keep track of bunch of values (the languages) without duplication?"""

list_of_languages = set()
with open('D://students.txt','r') as f:
    f_contents = f.readlines() [1:]
    for line in f_contents:
        line_updated = line.strip().split(':')
        if line_updated[1]:
            nickname_languages = line_updated[1]
            nickname_languages_updated = nickname_languages.strip().split(',')
            if nickname_languages_updated:
                for nick_lang_list in nickname_languages_updated:
                    nick_lang_list = nick_lang_list.strip()
                    if nick_lang_list:
                        if nick_lang_list[0].islower():
                            list_of_languages.add(nick_lang_list)
        else:
            continue
print(list_of_languages)
        
