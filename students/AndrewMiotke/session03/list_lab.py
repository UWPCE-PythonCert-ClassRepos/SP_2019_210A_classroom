#!/usr/bin/env python3
# https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/list_lab.html

# Series One
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit_list)

add_fruit = input("Type another fruit: ")
fruit_list.append(add_fruit)
print(fruit_list)

get_index = int(input("Type a number to get a fruit: "))
print(fruit_list[get_index - 1])

new_fruit_list = [add_fruit] + fruit_list
print(new_fruit_list)

insert_fruit = input("Insert a fruit: ")
fruit_list.insert(0, insert_fruit)
print(fruit_list)

for fruits_begining_with_p in fruit_list:
    if fruits_begining_with_p[0].lower() == "p":
        print(fruits_begining_with_p)

# Series Two
print(fruit_list)

fruit_list.pop()
print(fruit_list)

delete_fruit = input("What fruit would you like to delete? ")
fruit_list.remove(delete_fruit)
print(fruit_list)

# Series Three
for favorite_fruit in fruit_list:
    users_favorite_fruit = input(f"do you like {favorite_fruit.lower()}, yes or no? ")
    if users_favorite_fruit == "no":
        fruit_list.remove(favorite_fruit)
        print()
        print(fruit_list)
        print()
    elif users_favorite_fruit != "yes" or "no":
        print(fruit_list)

# Series Four
reversed_list = fruit_list
for reverse in reversed(reversed_list):
    print(reverse[::-1])