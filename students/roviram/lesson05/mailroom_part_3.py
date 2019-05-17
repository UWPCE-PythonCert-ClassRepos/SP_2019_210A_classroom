#------------------- Script Details-----------------------------------------------------------#
# Week 4 Homework: Mailroom Part 3
# Miguel Rovira-Gonzalez, 5/12/19, Updating Mailroom to have error handling and comprehensions
#-----------------------------------------------------------------------------------------------#
"""Part 1 Goal: Create a list of your donors and a history of the amounts they have donated: e.g  ([Miguel, 100], [Emma, 100, 200])
    A) The list needs to hold to have at least 5 donors and 1-3 donations.
    B) The script should prompt the user (you) to choose from a menu of 3 actions:
        1) “Send a Thank You”,
        2) “Create a Report”
        3)  Quit Program
Put your main interaction into an if __name__ == '__main__' block.
"""

donors = {
        # Each Row represents 1 element
        "Miguel Rovira": [100.0, 200.0, 300.0, 400.0, 500.0],
        "Emma DaFoe": [200.0, 40520.0, 5000.0, 100.0, 400.0],
        "Pepper": [5.0, 20.0, 100.0],
        "Vicky Gonzalez": [600.0, 9000.0, 10.0],
        "Cristina Rovira": [25.0, 50.0, 75.0]
}
# Processing


def gen_stats(donors_dict):
    """Generating stats of the donors"""
    gen_list = []
    for donor in donors_dict:
        total = sum(donors_dict[donor])
        number_of_donations = len(donors_dict[donor])
        avg = round(total / number_of_donations, 2)
        stats = [donor, total, number_of_donations, avg]
        gen_list.append(stats)
    return gen_list


def create_report(report_donors):
    """Creating a report of the mail room donors"""
    stats_list = gen_stats(report_donors)
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
    list_answer = ""
    while True:
        while True:
            list_answer = input("\nWant to see the list of donors to send a 'Thank You' too? (type 'Yes' or 'No ') "
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


def send_letters(donors_dict):
    """
    :param donor_name: name of the donor in our database
    :param donation_amount: the amount the donor donated
    """

    for donor in donors_dict:
        with open(donor + ".txt", "w") as file_output:
            file_output.write(f"""Dear {donor},
Thank you for your most recent generous donation of ${donors_dict[donor][-1]}.

Sincerely,

The Mailroom Team""")

#".format(donor, donors_dict[donor][-1]))
    print("\nWe have sent letters to all the donors! ")


def main_menu():
    """This is displaying the main menu"""
    while True:
        try:
            menu_answer = int(input(
                "\nPlease choose from the following three options (please type 1, 2, 3, or 4):\n"
                "1) Send a 'Thank You' note to a single donor \n"
                "2) Create a Report \n"
                "3) Send letters to all donors \n"
                "4) Quit "))
        except ValueError:
            print("\nThat's an incorrect input (it must be an integer), Please type 1, 2, 3, or 4)")
            continue

    # Thank You Note
        if menu_answer == 1:
            thank_you()
            # Create a Report
        elif menu_answer == 2:
            create_report(donors)
        elif menu_answer == 3:
            send_letters(donors)
        elif menu_answer == 4:
            break


# Input / Output
if __name__ == '__main__':
    intro()
    main_menu()
