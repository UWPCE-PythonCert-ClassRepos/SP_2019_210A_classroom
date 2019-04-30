

# SERIES 1

fruits = ["Apples", "Pears", "Oranges", "Peaches"]

# Display the actual list
def list_fruits():

    print("The actual Fruit List is: ")
    for fruit in fruits:
        print(fruit)

    return fruits

# Ask and add a new fruit to Fruit list
def new_fruit():
    new_fruit = input("Which fruit would you like to add to this list?")
    fruits.append(new_fruit)


# Return fruit by index list_name.index(element, start, end)
def find_fruit():
    position = int(input("What position in the list are you looking for? Example: 1"))

    #verify if position exist on the list
    # if position is larger than size of the list, return error message
    if position >= len(fruits):
        print("position not valid in list")

    return position, fruits[position-1]


# Add another fruit to the beginning of the list using “+” and display the list.
def add_with_plus(fruits, added_fruit):

    fruits = [added_fruit] + fruits

    return fruits

# Add another fruit to the beginning of the list using insert()
def add_with_insert():

    fruits.insert(0, "Papaya")
    #list_fruits()

# Display all the fruits that begin with “P”, using a for loop.
def start_with_p():
    print("The fruits in the list that start with 'P' are:")
    for fruit in fruits:
        if fruit[0] == "P":
            print(fruit)


# Display the list
list_fruits()

# Ask the user for another fruit, add it to the end of the list and display list
new_fruit()

pos,returned_fruit = find_fruit()
print(pos, returned_fruit)
# Add another fruit to the beginning of the list using “+” and display the list.
list_fruits()
fruits = add_with_plus(fruits, 'Grape')
list_fruits()

# Add another fruit to the beginning of the list using insert()
add_with_insert()

# Display all the fruits that begin with “P”, using a for loop.
start_with_p()


# _____________________________________________________________

# SERIES 2

# Display the list.
list_fruits()

# Remove the last fruit from the list.
del fruits[-1]

# Display the list.
list_fruits()

# Ask the user for a fruit to delete, find it and delete it.
delete = input("which fruit would you like to delete?")
if delete in fruits:
    fruits.remove(delete)

list_fruits()


# SERIES 3

# Ask the user for input displaying a line like “Do you like apples?”
while True:
    for fruit in fruits:
        answer = input("Do you like " + fruit.lower() + "? (yes/no)")
        if answer.lower() == "yes":
            print("Nice!")
        # For each “no”, delete that fruit from the list.
        if answer.lower() == "no":
            print("Deleting " + fruit.lower() + " from the list")
            fruits.remove(fruit)
        else:
            print("Your answer should be 'yes' or 'no'.")

# Display the list.
list_fruits()


# SERIES 4

# all the letters in each item reversed
newFruits = []
print("The reversed copy of fruits list:")
for fruit in fruits:
    reverse = (fruit[::-1])
    #print(reverse)
    newFruits.append(reverse)
    print(fruit[::-1])


# Delete the last item of the original list. Display the original list and the copy.
del fruits[-1]
print("Original list: ",  fruits)
print("Reversed copy: ", newFruits)