# part one

import pathlib

print(pathlib.Path('./').absolute())


# part two

with open('students.txt', 'r') as in_file:
    in_file.readline()
    try_list = []
    for line in in_file:
        var1 = line.split(':')

        try_list.append(var1)
    print(try_list)

