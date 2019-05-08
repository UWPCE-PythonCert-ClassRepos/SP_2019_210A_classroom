#!/usr/bin/env python3

#Dictionaries 1:
first_dict = {"name":"Chris","city":"Seattle","cake":"Chocolate"}
print(first_dict)
del first_dict["cake"]
print(first_dict)
first_dict.update({"fruit":"Mango"})
print(first_dict.keys())
print(first_dict.values())
if "cake" not in first_dict.keys():
    print("Cake is not in dictionary")
if "Mango" in first_dict.values():
    print("mango in values")

#Dictionaries 2:
first_dict = {"name":"Chris","city":"Seattle","cake":"Chocolate"}
new_dict = {}
for ky,vl in first_dict.items():
    # Using loops --------
    # t_num = 0
    # for letter in vl:
    #     if letter.lower() == "t":
    #         t_num+=1
    # new_dict.update({ky:t_num})
    # Using list and count method 
    new_dict.update({ky:list(vl).count("t")})
print(new_dict)

#Sets 1:
s2 = set()
s3 = set()
s4 = set()
for num in range(21):
    if num %2 == 0 and num %4 == 0:
        s4.add(num)
    if num%2 == 0:
        s2.add(num)
    if num %3 == 0:
        s3.add(num)
print(s2,s3,s4)
def chk_subset(st1,st2):
    for num in st1:
        if num not in st2:
            return False
    return True

print(f"s3 is a subset of s2: {chk_subset(s3,s2)}")
print(f"s4 is a subset of s2: {chk_subset(s4,s2)}")

#Sets 2:
py_set = set("Python")
py_set.add("i")
print(py_set)
mar_frozen_set = frozenset("marathon")
print(py_set.union(mar_frozen_set))
print(py_set.intersection(mar_frozen_set))