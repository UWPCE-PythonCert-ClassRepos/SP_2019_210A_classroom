fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

def list_creator():
    answer = input("a prompt for the user > ")
    if answer == '1':
        thank_you()
    elif answer == '2':
        report()
    elif answer == '3':
        sys.exit(0)
    else:
        print("please answer 1, 2 or 3")

if __name__ == '__main__':
    list_creator()
    
