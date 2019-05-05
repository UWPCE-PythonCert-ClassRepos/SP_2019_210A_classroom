"""
Dictionaries 1
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes 
“Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True).

Dictionaries 2
Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s 
in each value as the value (consider upper and lower case?).

Sets
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).

Sets 2
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
display the union and intersection of the two sets.

"""




student_info = {"name": "George", "city": "Kent", "cake": "Chocolate"}
student_info2 = {"name": "George", "city": "Kent", "cake": "Chocolate"}


def show_dict(dct):
    for k, v in dct.items():
        print("{:<1}: {:<10}".format(k, v))
    print("\n")
    return 

def dictionaries_1(dct):

    print("\nDictionary")
    show_dict(dct)
    dct.pop("cake")
    print("\nDictionary with cake removed")
    show_dict(dct)
    dct.update(fruit = "Mango")
    print("\nDictionary with 'fruit' added")
    show_dict(dct)
    print("\n{x} {y} {x}".format( x = "*"*10, y = "END"))
       
    if "cake" in dct:
        print("GOT ME SOME!")
    else:
        print("NO CAKE!!")
    
    
    if "Mango" in dct.values():
        print("I got some Mango's!!!\n")
    else:
        print("no mango's here")

    
def dictionaries_2(dct):
    
    for key in dct.keys():
        t_count = 0
        for val in dct[key]:
            if val.lower() == 't':
                t_count += 1
        dct[key] = t_count
    show_dict(dct)

def sets():
    s2 = set()
    s3 = set()
    s4 = set()
    for x in range(0, 21):
        if x % 2 == 0:
            s2.add(x)
        if x % 3 == 0:
            s3.add(x)
        if x % 4 == 0:
            s4.add(x)
    print(s2)
    print(s3)
    print(s4)
    print("is s3 a subset of s2?: ", s3.issubset(s2))
    print("is s4 a subset of s2?: ", s4.issubset(s2))

def sets_2():
    py = set(['p','y','t','h','o','n','i'])
    fset = frozenset(['m','a','r','a','t','h','o','n'])
    set_union = py | fset
    print("py union fset", set_union)
    print("py intersection fset: ", py.intersection(fset))


def main():
    dictionaries_1(student_info)
    dictionaries_2(student_info2)
    sets()
    sets_2()

if __name__ == "__main__": main()
    