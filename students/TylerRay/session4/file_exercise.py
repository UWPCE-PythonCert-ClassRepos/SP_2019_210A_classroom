# Write a program which prints the full path for all files in the current directory, one per line. Use either the os module or pathlib.
# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command (you are essentially
# writing a simple version of the OS copy command)).
#     This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing).
#     Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
#     Test it with both text and binary files (maybe a jpeg or something of your choosing).
#     Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
#        This should only be a few lines of code :-)

import pathlib

pth = pathlib.Path('./')

def step_one():

    print("Step one: Write a program which prints the full path for all files in the current directory, one per line. Use either the os module or pathlib.\n")
    print("pth.is_dir() is:", pth.is_dir())
    print("pth.absolute() is",pth.absolute())
    print()
    print("The absolute path of each file in the working director are: ")
    for file in pth.iterdir():
        return(file.absolute())

def step_two():
    print("\n\nPart Two: Opening 'sherlock_small.txt' and saving the contents in a\n"
          "new file, in this case 'sherlock_small_new.txt'.\n\n")
    with open("sherlock_small.txt", 'rb') as infile, open("sherlock_small_new.txt", 'wb+') as outfile:
        outfile.write(infile.read())

def step_three():
    instruction = "\n\nPart Three: Printing a list of all the languages each student in a file know without duplicating languages.\n\n"
    failed = "I could not get this one and in the end copied so much of other students work that it didn't feel right to submit it on my behalf"
    print(instruction, failed)


if __name__ == '__main__':
    step_one()
    step_two()
    step_three()