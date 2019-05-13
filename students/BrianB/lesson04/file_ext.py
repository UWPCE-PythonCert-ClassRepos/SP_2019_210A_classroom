#! bin/usr/env python3

'''
Goal:

Get a little bit of practice with handling files and parsing simple text.

Paths and File Processing
    XXX
    XXX
        
        Advanced: make it work for any size file: i.e. don’t read the 
        entire contents of the file into memory at once. This should work
            for any kind of file, so you need to open the  files in 
            binary mode: open(filename, 'rb') (or 'wb' for writing). 
        Note that for binary files, you can’t use readline() – lines don’t 
            have any meaning for binary files.
        Test it with both text and binary files (maybe jpeg or something
            of your choosing).


File reading and parsing:

Download this text file:  students.txt

In it, you will find a list of names and what programming languages they
    have used in the past. This may be similar to a list generated at the
    beginning of this class.

Write a little script that reads that file, and generates a list of all
    the languages that have been used.

What might be the best data structure to use to keep track of bunch of
    values without duplication?

The file format:

The first line of the file is:

Name: Nickname, languages

And each line looks something like this:

Jagger, Michael: Mick, shell, python

So a colon after the name, then the nickname, and then one or more languages.

However, like real data files, the file is NOT well-formed. Only some 
lines have nicknames, and other small differences, so you will need to write 
some code to make sure you get it all correct.

Extra challenge: keep track of how many students specified each language.
'''

#import os
#import glob

#def file_path():
#    """Finds python files and Returns their directory."""
#
#    for item in glob.glob('**.py'):
#        print(os.path.abspath(item))
#    return


#def src_dst():
#    """Copies 'break_me.py' and moves it to an alternate directory."""
#
#    os.popen('cp ~/SP_2019_210A_classroom/students/BrianB/lesson01/break_me.py\
#                ~/SP_2019_210A_classroom/students/BrianB/lesson04/break_me.py')
#    return


def prog_langs():
    """Reads "students.txt" and Returns programming
        languages known by the students."""

    for line in open('students.txt'):
        for language in line.split(": "):
            if language == language.lower():
                print([language])
                break


#file_path()
#src_dst()
prog_langs()





