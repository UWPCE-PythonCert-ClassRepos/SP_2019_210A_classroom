#------------------- Script Details--------------------------------------#
# Week 3 Homework: List Lab
# Miguel Rovira-Gonzalez, 4/30/19, Created the List Lab Script
#-----------------------------------------------------------------------#

# Series 1
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

def show_fruit(fruit_list):
    print("\nHere is our fruit list:")
    for index, fruit in enumerate(fruit_list):
        print(str(index + 1) + ".", fruit)

def fruit_addition_end():
    user_fruit = input("\nLet's add another fruit to the end of our list: ")
    return user_fruit

def fruit_addition_beginning():
    user_fruit = input("\nLet's add another fruit to our list to the very beginning of our list: ")
    return user_fruit

def series_one(fruit_list):
    show_fruit(fruit_list)
    fruit_list.append(fruit_addition_end())
    show_fruit(fruit_list)
    number_user = int(input("Please enter a number and I will show you the corresponding fruit associated with it: "))
    print(fruit_list[number_user - 1])
    #second_fruit = input("Let's add another fruit to our list to the very beginning of our list: ")
    fruit_list = [fruit_addition_beginning()] + fruit_list
    show_fruit(fruit_list)
    fruit_list.insert(0, fruit_addition_beginning())
    show_fruit(fruit_list)
    print("Here are fruits starting with the letter 'P'")
    for fruit in fruit_list:
        if fruit.startswith("P"):
            print(fruit)


def remove_fruit(fruit_list):
    show_fruit(fruit_list)
    while True:
        delete_fruit = input("We are going to remove a fruit, please select which one to remove: ")
        if delete_fruit not in fruit_list:
            print("Not valid")
        else:
            print("Deleting Item")
            fruit_list.remove(delete_fruit)
            show_fruit(fruit_list)
            break


def series_two(fruit_list):
    remove_fruit(fruit_list)

# Series 3
def series_three(fruit_list):
    while True:
        for fruit in fruit_list:
            while True:
                fruit_like_response = input("Do you like " + fruit + "?" + " Please type 'yes' or 'no' ")
                if fruit_like_response.lower() == 'yes' or fruit_like_response.lower() == 'no':
                    break
                else:
                    continue
            if fruit_like_response.lower() == 'no':
                fruit_list.remove(fruit)

        show_fruit(fruit_list)
        return False

def series_four(fruit_list):
    reversed_list = []
    for fruit in fruit_list:
        print(fruit[::-1])
        reversed_list.append(fruit)

    print(reversed_list)
# Main Method
def main_body():
    series_one(fruit_list)
    series_two(fruit_list)
    series_three(fruit_list)
    series_four(fruit_list)

if __name__ == "__main__":
    main_body()











