#Task 1

given = (2, 123.4567, 100000, 12345.67)

print("file_" + "0"*(3-len(str(given[0]))) + "{} :   {}, {:.2e}, {:.2e}".format(given[0],round(given[1],2),given[2],given[3]))

#Task 2

print("file_" + "0"*(3-len(str(given[0]))) +f"{given[0]} :   {round(given[1],2)}, {given[2]:.2e}, {given[3]:.2e}")

#Task 3

def formatter(args):
    return (f"the {len(args)} numbers are:" + " {:d},"*(len(args)-1)) + " {:d}"

t= (1,2,3,4,5,6,7)
print(formatter(t).format(*t))

#Task 4
t = (4,30,2017,2,27)

print(f"0{t[3]} {t[4]} {t[2]} 0{t[0]} {t[1]}")

#Task 5

lst = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of the {lst[0][:-1]} is {lst[1]} and the weight of a {lst[2][:-1]} is {lst[3]}")

#Task 6

lst = ['First','$91239.01','Second','$8.09']
print(f"{lst[0]:<8}{lst[1]:<15}{lst[2]:<8}{lst[3]:<8}")