#!/usr/bin/env python3


donors = [("Alpha Beta", [1000.21, 250.80]),
          ("Tucker Jones", [800.33]),
          ("Vladmir Putin", [500000.12, 250000.55, 750000]),
          ("Kim Jong Il", [200.80]),
          ("Tony Robinson", [500000, 1000000, 750000])]

donor = donors[0]
donations = donors[1]

def main_menu():
    '''
    Main menu for the program.
    Will loop through and requests input until 3 is entered and then quits.
    1 will allow an addition of a donator, a new donation and the printing of a thank you letter
    2 will print a report of the donators and their donations as well as their average donation.
    '''
    while True:
        choice = input("""What would you like to do?
            1: Send a thank you
            2: Create a Report
            3: Quit
            >>>""").strip()
        if choice == "1":
            # leads to the thank_you function
            thank_you()
        elif choice == "2":
            # leads to the report function
            for line in report():
                print(line)
        elif choice == "3":
            # breaks the loop effectively exiting the program
            print("Quitting...")
            break
        else:
            # if the item is not 1, 2, or 3, will print this and go back to beginning of while loop
            print(("You replied {}, please reply with 1, 2 or 3").format(answer))


def thank_you():
    donor_input = input("Enter full name of donor else type 'list' to see donor list: ")
    if donor_input == 'list':
        for donor in donors:
            print(donor)


    else:
        # Search if repeat donor
        exists = False
        for donor in donors:
            if donor[0] == donor_input:
                donor_input = donor[0]
                exists = True
        if exists:
            pass
        else:
            donors.append((donor_input, []))

        # Add new donation
        donation = int(input("Enter donation amount: "))
        for donor in donors:
            if donor[0] == donor_input:
                donor[1].append(donation)

        print("Esteemed Donors", '\n', '------------')
        for donor in donors:
            print(donor)
        print (f"Thank you {donor_input} for your generous donation of ${donation} from a charity")


def report():
    """
    return a report by adding a line for every name in the donor dictionary
    """
    report_list = ["Donor Name" + " " * 10 + "| Total Given " + "| Num Gifts " + "| Average Gift\n" + "-" * 60]

    for donor in donors:
        stats = []
        donations = donors[1]
        total = sum(donations)
        num = len(donations)
        stats.append((donor[0], total, num. total / num))
        print(stats)

    return donations


if __name__ == "__main__":
    print("Welcome to the Mailroom!")
    main_menu()