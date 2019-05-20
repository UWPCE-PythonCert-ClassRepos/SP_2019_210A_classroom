#------------------- Script Details-----------------#
# Week 3 Homework: Mailroom Part 1
# Miguel Rovira-Gonzalez, 4/27/19, created Part 1 of the mailroom program
#---------------------------------------------------#
"""Part 1 Goal: Create a list of your donors and a history of the amounts they have donated: e.g  ([Miguel, 100], [Emma, 100, 200])
    A) The list needs to hold to have at least 5 donors and 1-3 donations.
    B) The script should prompt the user (you) to choose from a menu of 3 actions:
        1) “Send a Thank You”,
        2) “Create a Report”
        3)  Quit Program
Put your main interaction into an if __name__ == '__main__' block.
"""

donors = [
        # Each Row represents 1 element
        ("Miguel Rovira", [100, 200, 300, 400, 500]),
        ("Emma DaFoe", [200, 40520, 5000, 100, 400]),
        ("Pepper", [5, 20, 100]),
        ("Vicky Gonzalez", [600, 9000, 10]),
        ("Cristina Rovira", [25, 50, 75]),
    ]

#donation_amount = []

# Processing
def gen_stats(donors):
    """Generating stats of the donors"""
    gen_list = []
    final_list = donors
    for donor in donors:
        donations = donor[1]
        total = sum(donations)
        number_of_donations = len(donations)
        avg = round(total / number_of_donations, 2)
        stats = [donor[0], total, number_of_donations, avg]
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

#create_report(donors)
def intro():
    """Welcoming the user to the application"""
    # Intro to the application
    print("Hello! Welcome to the mailroom! We are excited you are apart of our team.\n")

def thank_you():
    """Thanking the donor for their donor and adding a new donor if they are new"""

    while True:
        list_answer = input("\nThank you notes are always appreciated!\n"
                            "Want to see the list of donors to send a 'Thank You' too? (type 'Yes' or 'No ') ")
        # Cleaning up the Users Answer
        if list_answer.upper().strip() == 'YES':
            for donor in donors:
                print(donor)

        # Prompt Donor Name
        donor_name = input("\nPlease enter the donor name: ")

        print("You typed:", donor_name)
        match = False
        for donor in donors:
            if donor_name.lower() == donor[0].lower():
                print("\nCool, I found that donor")
                match = True
        #Checking if match is true
        if match:
            pass
        else:
            print("I didn't find that donor, I am adding them to our database now")
            donors.append((donor_name, []))

        donation_amount = float(input("\nHow much did they donate?: "))
        for donor in donors:
            if donor[0] == donor_name:
                donor[1].append(donation_amount)

        print()
        print("Time to send a thank you email!")
        print("Dear", donor_name + ",\n\n"
        "Thank you for your generous donation of", str(donation_amount) + ".", "\n\nEmail has been sent!")

        menu_answer = input("Are you done? ('Yes' or 'No' ) ")
        if menu_answer.upper().strip() == 'YES':
            break

def main_menu():
    """This is displaying the main menu"""
    while True:
        menu_answer = input(
            "\nPlease choose from the following three options (please type 1, 2, or 3):\n"
                   "1) Send a 'Thank You' note \n"
                   "2) Create a Report \n"
                   "3) Quit "
            )
        # Thank You Note
        if menu_answer.strip() == '1':
            thank_you()
        # Create a Report
        elif menu_answer.strip() == '2':
            create_report(donors)
        # Quit the Program
        elif menu_answer.strip() == '3':
            break

# Input / Output
if __name__ == '__main__':
    intro()
    main_menu()