"""
Write a program which prints the full path for all files in the current directory, one per line
Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing).
Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
Test it with both text and binary files (maybe jpeg or something of your choosing).
"""

import os, pathlib, pickle

lst_copy = []
obj_file = ""

def path():
    pth = pathlib.Path("./")
    print("\n", pth.absolute())
    for fle in pth.iterdir():
        print(fle)

def copy(filename):

    chunk_size = 10000
    with open(filename, "rb") as infile, open("2"+ filename, "wb") as outfile: 
        while True:
            contents = infile.read(chunk_size)
            if contents:
                outfile.write(contents)
            else:
                break
            



def reading_parsing():
    student_lst  = []
    with open("students.txt","r") as infile:
        for line in infile.readlines():
            row = line.strip().split(":")
            dct_row = {"Name": row[0], "Nickname": "", "languages": ""}
            if row[1].islower() == False:
                lst_row = row[1].split(",")
                # print(lst_row)
                lang = []
                name = []
                for word in lst_row:
                    if word.islower():
                        lang.append(word)
                    else:
                        name.append(word)
                dct_row.update(Nickname = str(name).strip().replace("[","").replace("]", "").replace("'",""), languages = str(lang).strip().replace("[","").replace("]", "").replace("'",""))
            else:
                dct_row.update(languages = row[1].strip())
            
                    
            student_lst.append(dct_row)
    idx = 0
    for row in student_lst:
        print("{:<2}: {:<25}-   {:^15} -{:>30}".format(idx, row["Name"], row["Nickname"], row["languages"]))
        idx += 1




def main():
    path()
    copy("mp2.jpg")
    reading_parsing()
if __name__ == "__main__": main()
    