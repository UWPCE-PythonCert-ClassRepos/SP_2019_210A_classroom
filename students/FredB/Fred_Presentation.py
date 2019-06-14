#!/usr/bin/env python

#FredBallyns
#Presentation

import sys, os, time

actually_clear = True
sleep_type = .1
sleep_erase = .05

presenter = "Fred Ballyns"
topic = "Python"
sub_topics = {
"Print statement settings": "If you don't want line to end with enter, use end=''. Also default object separator is sep=' '.",
"String Slicing": "Growing a string was done with print(seq[i],end=''). Deletion of final character was done using seq[:i] where 'i' is decreasing.",
"OS Module": f"There are {len(dir(os))} items in the os module. The two I'm using are 'os.name' and 'os.system'. Window name is 'nt' while Linux is 'posix'. Clear screen for windows system is 'cls' while linux is 'clear'.",
"Time Module": f"There are {len(dir(time))} items in the time module. 'time.sleep(.1)' is a 1/10 second pause."
}

opening_statement = f"Hello, \n\nMy name is {presenter} and this is my {topic} presentation. \nI will be discussing: \n\n"


def clear_screen(x=actually_clear):
    if x:
        #Windows 'nt'
        if os.name == 'nt':
            clearText="cls"
        #Linux 'posix'   
        else:
            clearText="clear"
        os.system(clearText)
        print("\n")


def type_text(input_text, x = sleep_type):
    for i in range(len(input_text)):
        time.sleep(x)
        print(input_text[i], end="")

def type_eraser(input_text, remain_text=0, x = sleep_erase):
    if type(remain_text) is str:
        remain_text = len(remain_text)
    remain_text = int(remain_text)
    len_str=len(input_text)
    for i in range(len_str):
        temp=input_text[:(len_str-i-1+remain_text)]
        time.sleep(x)
        clear_screen()
        print(temp, end="")

def hype_intro():
    print("\n"*5)
    clear_screen()
    phrases = ("a great.....","an amazing.....", "a supercalifragilisticexpialidocious presentation \n")
    
    prefix_phrase = "Get ready for "
    type_text(prefix_phrase)
    for i, j in enumerate(phrases):
        type_text(phrases[i])
        time.sleep(.5)
        if i == len(phrases)-1:
            type_text("\nHere we go !!!\n\n")
        else:
            type_eraser(prefix_phrase+phrases[i],prefix_phrase)
    time.sleep(1)
    for i in range(3, 0,-1):
        print(i)
        time.sleep(1)
    clear_screen()

def list_sub_topics():
       for i, j in enumerate(sub_topics):
        type_text(str(i+1)+". "+j)
        print("")
        time.sleep(2)

def print_topics():
    clear_screen()
    for i, j in enumerate(sub_topics):
        type_text(str(i+1)+f". {j}\n"+sub_topics[j])
        print("\n")
        time.sleep(3)
    time.sleep(4)
    clear_screen()    


def primes(n):
    i = 2
    seq=[]
    while i < n+1:
        while n % i ==0:
            seq.append(i)
            print(i)
            n = n / i
            i += 1
            print(seq)

def end_presentation():
    clear_screen()
    type_text("That was fun.\n\nHope you all enjoyed.\n\n ----The End----\n\n")


if __name__ == "__main__":
    hype_intro()
    type_text(opening_statement)
    list_sub_topics()
    print_topics()
    end_presentation()


    


