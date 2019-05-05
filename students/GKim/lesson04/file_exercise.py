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
obj_file = 

def path():
    pth = pathlib.Path("./")
    print("\n", pth.absolute())
    for fle in pth.iterdir():
        print(fle)



def main():
    # path()
    read_data(obj_file)
if __name__ == "__main__": main()
    