#------------------- Script Details--------------------------------------#
# Week 6 Homework: Mailroom Part 4
# Miguel Rovira-Gonzalez, 5/19/19, Updating Mailroom to have dict switch
# and made improvements in code from previous weeks feedback
#------------------------------------------------------------------------#

from sys import exit


donors = {
        # Each Row represents 1 element
        "Miguel Rovira": [100.0, 200.0, 300.0, 400.0, 500.0],
        "Emma DaFoe": [200.0, 40520.0, 5000.0, 100.0, 400.0],
        "Pepper": [5.0, 20.0, 100.0],
        "Vicky Gonzalez": [600.0, 9000.0, 10.0],
        "Cristina Rovira": [25.0, 50.0, 75.0]
}

# Processing


def gen_stats():
    """Generating stats of the donors"""
    gen_list = []
    for donor, donations in donors.items():
        total = sum(donations)
        number_of_donations = len(donations)
        avg = round(total / number_of_donations, 2)
        stats = [donor, total, number_of_donations, avg]
        gen_list.append(stats)
    return gen_list


def create_report():
    """Creating a report of the mail room donors"""
    stats_list = gen_stats()
    stats_list.sort(key=lambda stats_list: stats_list[1], reverse=True)
    print("{:<20} | {:^15} | {:>15} | {:>15}".format("Name of Donor", "Total Donation Amount", "Number of Donations", "Average Gift Amount"))
    print("-"*89)
    for index, donor in enumerate(stats_list):
        print(str(index + 1) + ".", "{:<20}${:^15}{:>15}\t\t\t\t{}{:>15}".format(donor[0], donor[1], donor[2], "$", donor[3]))


def intro():
    """Welcoming the user to the application"""
    # Intro to the application
    print("Hello! Welcome to the mailroom! We are excited you are apart of our team.\n")


def thank_you():
    """Thanking the donor for their donor and adding a new donor if they are new"""
    while True:
        while True:
            list_answer = input("Want to see the list of donors to send a 'Thank You' too? (type 'Yes' or 'No ') "
                                ).lower().strip()

        # Cleaning up the Users Answer
            if list_answer == 'yes':
                for donor in donors:
                    print(donor)
                break
            elif list_answer == 'no':
                break
            else:
                continue

        donor_name = input("\nPlease enter the donor name: ")

        # Prompt Donor Name
        print("You typed:", donor_name)
        match = False

        if donor_name in donors:
            print("Cool, I found that donor")
            match = True

        if not match:
            print("I didn't find that donor, I am adding them to our database now.")
            donors[donor_name] = []
        while True:
            try:
                donation_amount = float(input("\nHow much did they donate?: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        donors[donor_name].append(donation_amount)
        print("\nTime to send a thank you email!")
        print(f"""Dear {donor_name},

Thank you for your generous donation of ${donation_amount}.
Sincerely,

The Mailroom Team""")

        menu_answer = input("\nAre you done? ('Yes' or 'No' ) ").upper().strip()
        if menu_answer == 'YES':
            break


def send_letters():
    """
    :param donor_name: name of the donor in our database
    :param donation_amount: the amount the donor donated
    """

    for donor in donors:
        with open(donor + ".txt", "w") as file_output:
            file_output.write(f"""Dear {donor},
Thank you for your most recent generous donation of ${donors[donor][-1]}.

Sincerely,

The Mailroom Team""")
    print("\nWe have sent letters to all the donors! ")


dict_switch = {1: thank_you,
               2: create_report,
               3: send_letters,
               4: exit
               }


def main_menu():
    """This is displaying the main menu"""
    while True:
        try:
            menu_answer = int(input(
                "\nPlease choose from the following three options (please type 1, 2, 3, or 4): \n"
                "1) Send a 'Thank You' note to a single donor \n"
                "2) Create a Report \n"
                "3) Send letters to all donors \n"
                "4) Quit \n"))
            dict_switch[menu_answer]()
        except KeyError:
            print("That is not a valid option of the menu. Please type 1, 2, 3, or 4")
        except ValueError:
            print("""\nThat's an incorrect input, you typed in a string
(it must be an integer), Please type (1, 2, 3, or 4).""")
            continue


# Input / Output
if __name__ == '__main__':
    intro()
    main_menu()
