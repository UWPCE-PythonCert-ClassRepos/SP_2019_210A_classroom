#!/usr/bin/env python3
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

def series1(fruits):
    answer = input("Please pick a fruit to add > ")
    fruits.append(answer)
    print(fruits)
    answer = input("Please pick an integer > ")
    while not answer.isdigit() or int(answer) > len(fruits):
        answer = input("Please pick an integer > ")
    print(fruits[int(answer) - 1])
    answer = input("Please pick a fruit to add > ")
    new_fruit = [answer]
    fruits = new_fruit + fruits
    print(fruits)
    answer = input("Please pick a fruit to add > ")
    fruits.insert(0, answer)
    print(fruits)
    for f in fruits:
        if f[0] == 'P': print(f)

def series2(fruits):
    print(fruits)
    fruits.pop()
    print(fruits)
    answer = input("Please pick a fruit to delete > ")
    if answer in fruits:
        fruits.remove(answer)
    #bonus
    new_fruits = fruits * 2
    answer = input("Please pick a fruit to delete(bonus) > ")
    while answer not in new_fruits:
         answer = input("Please pick a fruit to delete(bonus) > ")
    for f in fruits:
        if f == answer:
            new_fruits.remove(f)

def series3(fruits):

    for f in fruits[:]:
        while True:
            answer = input("Do you like {} > ".format(f))
            if answer == 'yes':
                break
            elif answer == 'no':
                fruits.remove(f)
                break
            else:
                print("Please say 'yes' or 'no'.")
    print(fruits)

def series4(fruits):
    new_fruits = []
    for f in fruits:
        new_fruits.append(f[::-1])
    fruits.pop()
    print(fruits)
    print(new_fruits)

if __name__ == '__main__':

    print(fruits)
    series1(fruits)
    series2(fruits)
    series3(fruits)
    series4(fruits)
