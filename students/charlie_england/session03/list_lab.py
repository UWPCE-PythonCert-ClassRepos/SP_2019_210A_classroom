#!/usr/bin/env python3
print("working")

#Series 1
lst = ["Apples", "Pears", "Oranges","Peaches"]
print(lst)
lst.append(input("Please add another fruit"))
print(lst)
user_input = input("Please enter a number >>>")
print(f"{user_input} cooresponds to {lst[int(user_input)-1]}")
#add another fruit to the beginning of the list using +?
lst.insert(0,"Kiwis")
print(lst)
for fruit in lst:
    if fruit[0] == "P":
        print(fruit)

#Series 2
print(lst)
lst.pop()
print(lst)
fruit_delete = input("Please provide a fruit to delete >>>")
lst.remove(fruit_delete)
print(lst)
lst = lst*2
for fruit in lst:
    if fruit_delete == fruit:
        lst.remove(fruit_delete)
print(lst)

#Series 3
lst = ["Apples", "Pears", "Oranges","Peaches"]
liked_fruit = []
for fruit in lst:
    response =  input(f"Do you like {fruit.lower()}? yes/no >>>")
    while True:
        if response == "no":
            break
        elif response == "yes":
            liked_fruit.append(fruit)
            break
        else:
            response = input(f"You inputted {response}, please use yes or no. Do you like {fruit.lower()}? >>>")
print(liked_fruit)

#Series 4
lst = ["Apples", "Pears", "Oranges","Peaches"]
new_lst = []
for fruit in lst:
    new_lst.append(fruit[::-1])
lst.pop()
print(lst)
print(new_lst)
