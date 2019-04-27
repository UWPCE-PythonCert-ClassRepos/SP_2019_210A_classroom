#!/usr/local/bin/python3
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

def series1():
    answer = input("Please pick a fruit to add > ")
    fruits.append(answer)
    print(fruits)
    answer = input("Please pick an integer > ")
    while type(answer) is not int or answer > len(fruits):
        answer = input("Please pick an integer > ")
    print(fruits[answer - 1])
    answer = input("Please pick a fruit to add > ")
    new_fruit = [answer]
    fruits = new_fruit + fruits
    print(fruits)
    answer = input("Please pick a fruit to add > ")
    fruits.insert(0, answer)
    print(fruits)
    for f in fruits:
        if f[0] == 'P': print(f)

def series2():
    print(fruits)
    fruits.pop()
    print(fruits)
    answer = input("Please pick a fruit to delete > ")
    if answer in fruits:
        fruits.delete(answer)
    #bonus
    new_fruits = fruits * 2
    for f in fruits:
        if f == answer:
            fruits.delete(f)

def series3():
    for f in fruits:
        while True:
            answer = input("Do you like {}".format(f))
            if answer == 'yes':
                break
            elif answer == 'no':
                fruits.delete(f)
                break
            else:
                print("Please say 'yes' or 'no'.")
    print(fruits)

def series4():
    new_fruits = []
    for f in fruits:
        new_fruits.append(f[::-1])
    fruits.pop()
    print(fruits)
    print(new_fruits)

if __name__ == '__main__':
    print(fruits)
    series1()
    series2()
    series3()
    series4()
