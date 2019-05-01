#!/usr/bin/env python3.7.3

#List lab
#FredBallyns
#Session03


def series1():
    fruits1=['Apples','Pears', 'Oranges','Peaches']
    print(fruits1)
    fruits1.append(input('Name another fruit: '))
    print(fruits1)
    fruit_no = int(input('Enter a number from 1-5: '))
    print("Fruit number ",fruit_no," is ",fruits1[fruit_no -1])
    fruits1 = ['Kiwi'] + fruits1
    print (fruits1)
    fruits1.insert(0,'Pineapple')
    print(fruits1)
    for fruit in fruits1:
        if fruit.upper().startswith('P'):
            print(fruit)
    print("Done with Series1", '\n')
    return fruits1


def series2(fruits1):
    fruits2=fruits1[:]
    print(fruits2)
    fruits2.pop()
    print(fruits2)
    fruit_remove = input('Enter a fruit to remove: ')
    fruits2.remove(fruit_remove)
    print(fruits2)
    print("Done with Series2", '\n')


def series3(fruits1):
    fruits3=fruits1[:]
    print(fruits3)
    for fruit in fruits1:
        go = True
        while go:
            response = input(f"Do you like {fruit.lower()} ? (yes/no): ")
            if response.lower() == "yes" or response.lower() == "y":
                go = False
            elif response.lower() == "no" or response.lower() == "n":
                fruits3.remove(fruit)
                go = False
            else:
                print("yes or no only")
    print(fruits3)
    print("Done with Series3", '\n')


def series4(fruits1):
    print(fruits1)
    fruits4 = [fruit[::-1] for fruit in fruits1]
    print(fruits4)
    print("Done with Series4", '\n')




if __name__ == "__main__":
    fruits1 = series1()
    series2(fruits1)
    series3(fruits1)
    series4(fruits1)