#!/usr/bin/env python3

# Series 1
print("\nSeries 1\n")
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)
new_fruit = input("\nProvide the name of a fruit to add to the list:\n")
fruit_list.append(new_fruit)
print(fruit_list)
fruit_index = int(input("\nProvide the index of a fruit (starting with 1, not 0):\n"))
print("You chose fruit index {} ({}): {}".format(fruit_index, fruit_index - 1, fruit_list[fruit_index - 1]))
print("\nAdding 'Grapes' to the beginning of the list...")
fruit_list = ["Grapes"] + fruit_list
print(fruit_list)
print("\nInserting 'Mangos' at the beginning of the list...")
fruit_list.insert(0, 'Mangos')
print(fruit_list)
print("\nDisplaying all fruits that being with 'P'...")
for fruit in fruit_list:
    if fruit[0] == 'P':
        print(fruit)

# Series 2
print("\nSeries 2\n")
print(fruit_list)
print("\nRemoving the last fruit from the list...")
fruit_list.pop(-1)
print(fruit_list)
fruit_to_delete = input("\nProvide the name of a fruit to delete from the list:\n")
fruit_list = [f for f in fruit_list if f != fruit_to_delete]
print(fruit_list)

# Series 3
print("\nSeries 3\n")
new_fruit_list = []
for i in range(len(fruit_list)):
    while True:
        answer = input("Do you like {}?  Answer yes or no.\n".format(fruit_list[i].lower()))
        if answer.lower() == 'no':
            break
        elif answer.lower() == 'yes':
            new_fruit_list.append(fruit_list[i])
            break
print(new_fruit_list)

# Series 4
print("\nSeries 4\nReversing the text of each fruit")
reversed_fruit_list = [fruit[::-1] for fruit in new_fruit_list]
print(reversed_fruit_list)
new_fruit_list.pop(-1)
print(new_fruit_list)