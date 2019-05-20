#!/usr/bin/env python3

first_name = "andrew,gus,maggie".split(",")
last_name = "miotke,gus,saunders".split(",")

for i in zip(first_name, last_name):
    print(i)


zipper = zip(range(20), range(20, 40))
print(zipper)
for n in zipper:
    print(n)

formatted_string = "{:.>20}".format("${:,.2f}".format(123.3214))
print(formatted_string)

formatted_string_two = "Just some {:.>20} formatting".format("")
print(formatted_string_two)

