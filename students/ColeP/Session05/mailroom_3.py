# Mailroom Yo

donors = {"Donny Donor": [100, 10, 45],
          "Gav Giver": [12, 16, 20],
          "Stingy Steve": [2, 5, 1],
          "Freaky Frank": [1200, 999, 1005],
          }


def thanks():
    name_in = input('Who would you like to thank?\nPlease pick a name. Enter "List" to see names\n')
    if name_in == 'List':
        for i in donors:
            print(i)
        thanks()
    elif name_in in donors:
        try:
            don_am = int(input('How much did they give?\n'))
            donors[name_in] += [don_am]
            thank_u_letter(name_in, don_am)
        except ValueError:
            print("Input must be an integer, try again.\n\n")
            thanks()
    else:
        try:
            don_am = int(input('How much did they give?\n'))
            donors[name_in.title()] = [don_am]
            thank_u_letter(name_in, don_am)  # add the input amount
        except ValueError:
            print("Input must be an integer, try again.\n\n")
            thanks()


def thank_u_letter(name, amount):
    return ('''
Dear {},

Thank you for generous donation of ${:.2f} to The Org!

-The Org
    '''.format(name, amount))


def take_total(item):  # used in conjunction with sorted() to take the donations and sort by total donation
    return item[1]


def gen_stats_print(in_dict):  # prints donor Name, sum of donations, and average donation, formats
    """
    :param in_dict: takes donor list, sums and takes number of donations, sorts based on sum
    :return: prints formatted table

    """
    compy = [(donor, sum(in_dict[donor]), len(in_dict[donor]), sum(in_dict[donor]) / len(in_dict[donor])) for donor in
             in_dict]
    sorted_donors = sorted(compy, key=take_total, reverse=True)  # sorts the donor list by their contribution totals
    print()
    print("{:22s} _ {:11s} _ {:9s} _ {:12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print()
    for row in sorted_donors:
        print('{:22s} ${:11.2f} {:^13}$ {:>12.2f}'.format(*row))
    print()


def letter4all():
    for i in donors:
        with open('{}.txt'.format(i), 'w+') as let:
            let.writelines(thank_u_letter(i, sum(donors[i])))


# def quit_it():
#     print('Quitting')
#     sys.exit()


def main_menu():
    while True:
        answer = input('''Choose an Option:
    1. Send a Thank You
    2. Create a Report
    3. Write Letters to all donors
    4. Quit 
    ''')

        answer = answer.strip()
        if answer == '1':
            print(thanks())
        elif answer == '2':
            gen_stats_print(donors)
        elif answer == '3':
            # letter to all
            letter4all()
        elif answer == '4':
            break
            # quit_it()
        else:
            print('Please enter 1, 2 or 3')


if __name__ == "__main__":
    print('Welcome to the Mailroom')

    main_menu()

