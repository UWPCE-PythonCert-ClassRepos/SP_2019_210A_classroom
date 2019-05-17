# Mailroom Yo

donors = [("Donny Donor", [100, 10, 45]),
          ("Gav Giver", [12, 16, 20]),
          ("Stingy Steve", [2, 5, 1]),
          ("Freaky Frank", [1200, 999, 1005]),
          ]


# # adding another donation:
# donors[0][1].append(69)
#
# print(donors)

# # removing a donation:
# donors[0][1].pop()
#
# print(donors)
# formatting:
# "{:.2f}".format(123.666666667) -> 12422.67

def thanks():
    name_in = input('Who would you like to thank?\nPlease pick a name. Enter "List" to see names\n')
    if name_in == 'List':
        for i in donors:
            print(i[0])
        thanks()
    elif name_in in donors:
        donors[0][1].append(int(input('How much did they give?')))
        print('Thank you ' + name_in + ' for your donation!')
    # elif name_in == 'Gav Giver':
    #     donors[1][1].append(int(input('How much did they give?')))
    #     print('Thank you ' + name_in + ' for your donation!')
    # elif name_in == 'Stingy Steve':
    #     donors[2][1].append(int(input('How much did they give?')))
    #     print('Thank you ' + name_in + ' for your donation!')
    # elif name_in == 'Freaky Frank':
    #     donors[3][1].append(int(input('How much did they give?')))
    #     print('Thank you ' + name_in + ' for your donation!')
    else:
        donors.append((name_in, []))
        donors[int(len(donors)-1)][1].append(int(input('How much did they give?')))
        print('Thank you ' + name_in + ' for your donation!')


def take_total(item):  # used in conjunction with sorted() to take the donations and sort by total donation
    return sum(item[1])

# sorted_donors = sorted(donors, key=take_total, reverse=True)  # sorts the donor list by their contribution totals


def gen_stats(n):  # prints donor Name, sum of donations, and average donation, formats
    sorted_donors = sorted(donors, key=take_total, reverse=True)  # sorts the donor list by their contribution totals
    total = sum(sorted_donors[n][1])
    num = len(sorted_donors[n][1])
    stats = str((sorted_donors[n][0], total, num,  total//num)).strip('()').split(',')
    stats_formatted = stats[0].strip("''").ljust(21) + '$' + stats[1].rjust(10) + stats[2].rjust(12) + ' $' + stats[3].\
        rjust(12)
    return stats_formatted


def report():  # runs gen_stats and prints for each, finishes string formatting

    header = ('Name' + ' ' * 16 + 'Total Given . Num Gifts . Average Gift')
    print(header)
    print('.' * len(header))

    for i in range(len(donors)):
        print(gen_stats(i))

    print()


# def quit_it():
#     print('Quitting')
#     sys.exit()


def main_menu():
    while True:
        answer = input('''Choose an Option:
    1. Send a Thank You
    2. Create a Report
    3. Quit 
    ''')

        answer = answer.strip()
        if answer == '1':
            thanks()
        elif answer == '2':
            report()
        elif answer == '3':
            # quit_it()
            break
        else:
            print('Please enter 1, 2 or 3')


if __name__ == "__main__":
    print('Welcome to the Mailroom')

    main_menu()

