#!/usr/bin/env python3

#
#Week 3 Homework 2
#list_lab
# https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/list_lab.html
#
#

def Series_1():
    a_list = ["Apple","Pear","Orange","Peach"]

    user_input_fruit = input("Please tell me a fruit in your mind: ")
    
    a_list.append(user_input_fruit)
    print(a_list)
    
    user_input_index = int(input("Please tell me a number, I will tell you a fruit name: "))
    if user_input_index < len(a_list):
        print(a_list[user_input_index-1])
    else:
        print("I don't have that many of fruits.")

    #append the fruit you told me to the beginning of the list 
    print("I prepend {} to the beginning of the list".format(user_input_fruit))
    a_list.insert(0,user_input_fruit)
    print(a_list)

    for i in range(len(a_list)):
        if a_list[i][0] == "P":
            print(a_list[i])

def Series_2():
    a_list = ["Grape","Apple","Pear","Orange","Peach"]
    print(a_list)
    a_list.pop()
    print(a_list)
    user_input_to_delete = input("Please tell me a fruit to remove from this list: ")
    user_input_to_delete = user_input_to_delete.capitalize()
    a_list.extend(a_list)
    while not user_input_to_delete in a_list:
        user_input_to_delete = input("Please tell me a fruit to remove from this list: ")
        user_input_to_delete = user_input_to_delete.capitalize()

    a_list.remove(user_input_to_delete)
    print(a_list)

def Series_3():
    a_list = ["Grape","Apple","Pear","Orange","Peach"]
    for f in a_list:
        user_input = input("Do you like {} ?".format(f.lower()))
        user_input = user_input.lower()
        while not (user_input == "yes" or user_input == "no"):
            user_input = input("Please input 'yes' or 'no' ")
        if user_input == "yes":
            a_list[a_list.index(f)] = f.lower()
            print(a_list)
        else:
            a_list.remove(f)
            print(a_list)


def Series_4():
    a_list = ["Grape","Apple","Pear","Orange","Peach"]
    print(a_list)
    another_list = a_list
    for i in range(len(another_list)):
        another_list[i] = another_list[i][::-1]
    
    a_list.pop()
    print(another_list)

if __name__ == "__main__":
    Series_1()
    Series_2()
    Series_3()
    Series_4()
