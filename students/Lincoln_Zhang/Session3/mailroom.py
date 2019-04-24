#!/usr/bin/env python3
import sys

print("Mailroom")

def Thank_You():
    pass

def Report():
    pass

def Quit():
    sys.exit()

def main_menu():
    while True:
        answer = input("""
            Please tell me what do you want to do:
            1. Thank you
            2. Report
            3. Quit
            >>> 
            """)
        print("Your reply is ", answer)
        
        answer = answer.strip()
        if answer == "1":
            Thank_You()
        elif answer == "2":
            Report()
        elif answer == "3":
            Quit()
        else:
            print("Please input 1,2 or 3")


if "__name__" == "__main__":
    print("Welcome to mailroom!")
    main_menu()