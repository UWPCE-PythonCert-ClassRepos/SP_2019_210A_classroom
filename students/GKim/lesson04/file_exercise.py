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
            


def reading_parsing(file_name):
    """
    this organizes and get name nickname and languages  separated
    """
    student_lst  = []
    with open(file_name,"r") as infile:
        for line in infile.readlines():
            row = line.strip().split(":")
            dct_row = {"Name": row[0], "Nickname": "", "languages": ""}
            row_other_half = line.replace(' ', "").strip().split(":")[1].split(",")
            lang = []
            name = []
            for word in row_other_half:
                if word:
                    if word[0].islower():
                        lang.append(word)
                    else:
                        name.append(word)
                dct_row.update(Nickname = str(name).strip().replace("[","").replace("]", "").replace("'",""),
                                    languages = str(lang).strip().replace("[","").replace("]", "").replace("'",""))
                
            student_lst.append(dct_row)
    idx = 0
    for row in student_lst:
        print("{:<2}: {:<25}-   {:^15} -{:>30}".format(idx, row["Name"], row["Nickname"], row["languages"]))
        idx += 1

    """
    generating specific list of languages
    """
    
    generator = [item["languages"] for item in student_lst]
    specific_lang = []
    for lang in generator:
        line = lang.split(",")
        for x in line:
            if x:
                if x.strip() == "nothing":
                    continue
                if x.strip() not in specific_lang:
                    specific_lang.append(x.strip())
                    specific_lang.sort()

    print("\nSpecific Language list: \n")
    for index, language in enumerate(specific_lang):
            print(str((index + 1)) +".", language)

# def prog_langs(infile):
#     """Reads "students.txt" and Returns programming
#         languages known by the students."""
#     lang_list = []
#     for line in open(infile, "r"):
#         for language in line.strip().split(": "):
#              if language == language.lower():
#                 print([language])
#                 break
        
        
            
        

           


def main():
    path()
    copy("mp2.jpg")
    infile = "students.txt"
    reading_parsing(infile)
    # prog_langs(infile)
   
if __name__ == "__main__": main()
    