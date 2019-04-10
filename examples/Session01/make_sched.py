#!/usr/bin env python

import random

print("it works")

infile = open("students.txt")

names = []
infile.readline()
for line in infile:
    print(line)
    name = line.split(":")[0].strip()
    print(name)
    if name:
        names.append(name)

print(names)
random.shuffle(names)
print(names)

with open("light_sched.txt", 'w') as outfile:
    for week in range(2, 11):
        outfile.write("week {}\n".format(week))
        print("week {}".format(week))
        ind = (week - 2) * 2
        outfile.write(names[ind] + "\n")
        outfile.write(names[ind+1] + "\n")
        print(names[ind])
        print(names[ind+1])

