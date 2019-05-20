#------------------- Script Details----------------------------------#
# Week 4 Homework: Dict and Set Lab
# Miguel Rovira-Gonzalez, 5/4/19, Created the dict and set lab script
#--------------------------------------------------------------------#

# Data
student_attribute = {"Name": "Miguel", "City": "Seattle", "Cake": "Chocolate"}
student_attribute2 = {"Name": "Miguel", "City": "Seattle", "Cake": "Chocolate"}

def display_dictionary(dictionary):
    for dict_key, dict_values in dictionary.items():
        print("{:<1}:"" {}".format(dict_key, dict_values))

def dict_keys(dictionary):
    print("Here are the dictionary keys:", dictionary.keys())

def dict_values(dictionary):
    print("Here are the dictionary values:", dictionary.values())

def dict1(dictionary):
    display_dictionary(dictionary)
    dictionary.pop("Cake")
    print()
    display_dictionary(dictionary)
    dictionary["Fruit"] = "Mango"
    dict_keys(dictionary)
    dict_values(dictionary)
    # Testing for Key
    if "Cake" in dictionary:
        print("\nCake is still in the dictionary")
    else:
        print("\nCake is not in the dictionary anymore.")
    # Testing for Value
    if "Mango" in dictionary.values():
        print("Mango is a value in the dictionary.")

def dict2(dictionary):
    for dict_key in dictionary.keys():
        counter = 0
        for dict_val in dictionary[dict_key]:
            if "t" == dict_val.lower():
                counter += 1
        dictionary[dict_key] = counter
    display_dictionary(dictionary)


""""
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
"""
def first_sets():
    set2 = set()
    set3 = set()
    set4 = set()

    for number in range(0, 21):
        if number % 2 == 0:
            print(number, "is divisible by two")
            set2.add(number)
        if number % 3 == 0:
            print(number, "is divisible by three")
            set3.add(number)
        if number % 4 == 0:
            print(number, "is divisible by four")
            set4.add(number)
    print("\nChecking to see if set3 is a subset of set2 and that is:", set3.issubset(set2))
    print("Checking to see if set4 is a subset of set2 and that is:", set4.issubset(set2))

def second_set():
    py_set = set("Python")
    print(py_set)
    py_set.add("i")
    print(py_set)
    frozen_marathon_set = frozenset("Marathon")
    print(frozen_marathon_set)
    print("Here is the union of py_set and frozen_marathon_set:", py_set.union(frozen_marathon_set))
    print("Here is the intersection of py_set and frozen_marathon_set:", py_set.intersection(frozen_marathon_set))

def main():
    dict1(student_attribute)
    print()
    dict2(student_attribute2)
    first_sets()
    second_set()

if __name__ == '__main__':
    main()







