tpl1 = (2, 123.4567, 10000, 12345.67)

# Task 1
def printTuple(tpl1):
    v1 = "file_{0:03}: ".format(tpl1[0])
    v2 = "{0:.2f}".format(tpl1[1])
    v3 = "{:.2e}".format(tpl1[2])
    v4 = "{0:.2e}".format(tpl1[3])
    return f"{v1} {v2} {v3} {v4}"

print("Task 1")
print(printTuple(tpl1))


# Task 2
print("Task 2")
print("file_{:03}:  {:.2f} {:.2e} {:.2e}".format(*tpl1))


# Task 3
tpl2 = 12, 45, 22, 587, 97, 43, 32,

def formatter(tpl2):
    return (f"the {len(tpl2)} numbers are:" + " {:d},"*(len(tpl2)-1)) + " {:d}"

print("Task 3")
print(formatter(tpl2).format(*tpl2))


# Task 4

tpl3 = (4, 30, 2017, 2, 27)
# '02 27 2017 04 30'

print("Task 4")
print(f"0{tpl3[3]} {tpl3[4]} {tpl3[2]} 0{tpl3[0]} {tpl3[1]}")

# Task 5

list1 = ['oranges', 1.3, 'lemons', 1.1]

print("Task 5")
print(f"The weight of {list1[0]} is {list1[1]} and the weight of {list1[2]} is {list1[3]}")


#Task 6

list2 = ['First','$91239.01','Second','$8.09']

print("Task 6")
print(f"{list2[0]:<8}{list2[1]:<15}{list2[2]:<8}{list2[3]:<8}")