'''
Lesson: 02
Excercise: Fizz Buzz
Student Name: Jasneet Chandok
Last Update Date: 04/18/19
'''
#!/usr/bin/env python3.6


def fizz_buzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print ('FizzBuzz')
        elif num % 5 == 0:
            print ('Buzz')
        elif num % 3 == 0:
            print('Fizz')
        else:
        	print(num)

fizz_buzz()