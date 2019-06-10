from donor_models import Donor_Collection
from donor_models import Donor
import sys

def thank_you(donor_collection,new_don=None):
    """
    Send a Thank you to a single donor
    """
    while True:
        if not new_don:
            name_choice = input("Please input a name of an existing donor, enter 'l' for a list of donors, 'q' to go back to previous menu\n>>> ")
            norm_name_choice = name_choice.lower().strip().replace(" ","")
        else:
            norm_name_choice = new_don.lower().strip().replace(" ","")
        if norm_name_choice in donor_collection.donor_data.keys() or new_don:
            while True:
                try:
                    donation_amt = float(input(f"Please enter a donation amount for {donor_collection.donor_data[norm_name_choice].name}\n>>> "))
                    break
                    if donation_amt == "q":
                        break
                except ValueError:
                    print("That was an invalid, please try again, 'q' to head back to main menu")
            donor_collection.donor_data[norm_name_choice].add_donation(donation_amt)
            print(donor_collection.donor_data[norm_name_choice].send_thank_you())
            return donor_collection
        elif name_choice == "l":
            for donor in donor_collection.donor_data.values():
                print(donor.name)
        elif name_choice == "q":
                return donor_collection
        else:
            print(f'Could not find donor by the name of {name_choice}')

def thank_you_new(donor_collection):
    """
    Create a donor, and then send a thank you (use logic from the one function, send new_don ="yes")
    """
    while True:
        usr_name_input = input("Input a name of a new donor, 'q' to head back to main menu\n>>> ")
        norm_usr_name = usr_name_input.lower().strip().replace(" ","")
        if norm_usr_name in donor_collection.donor_data.keys():
            print(f"{usr_name_input} already in donors, please select a new name")
        elif usr_name_input == "q":
            return donor_collection
        else:
            break
    donor_collection.add_donor(Donor(usr_name_input))
    thank_you(donor_collection,new_don=usr_name_input)


def create_report(donor_collection):
    """
    create a report
    """
    print("Donor Name" + " "*11 + "|" + " "*3 + " Total Given " + " "*3 +
                   "| Num Gifts " + "| Average Gift\n" + "-"*60)
    for donor in donor_collection.donor_data.values():
        print(f"{donor.name:<20} $  {donor.total:>16,.2f} {donor.num_donations:^12} $ {donor.average:>10,.2f}")

def send_letters(donor_collection):
    """
    Send letters to all donors
    """
    for donor in donor_collection.donor_data.values():
        file_name = f"{donor.name}.txt"
        with open(file_name, "w") as fh:
            fh.writelines("""Dear {},\n\n 
        On behalf of Local Charity we would like to extend our sincerest thanks for your most recent ${} donation.\n
        Without people like you we could not continue blah blah blah\n
        Over time you have given us a total of ${:,.2f} over {} donation(s) which averages out to ${:,.2f} per donation! \n
        Again thank you\n
    Sincerely,\n
        Local Charity """.format(donor.name, donor.donations[-1], donor.total, donor.num_donations, donor.average))
        print(f'Created letter for {donor.name}')
        fh.close()
    print("Finished!")

def halt(pos_arg):
    """
    Quit..
    """
    print('quitting...')
    sys.exit()

def main():
    d1 = Donor("Jeff Bezos",[1000,500,20])
    d2 = Donor('blue berry',[1233,513])
    donor_collection = Donor_Collection([d1,d2])
    switch = {
        "1":thank_you,
        "2":thank_you_new,
        "3":create_report,
        "4":send_letters,
        "5":halt
    }
    
    while True:
        choice = input("""What would you like to do?
            1: Send a Thank You to a single existing donor
            2: Send a Thank You to a new donor
            3: Create a Report
            4: Send letters to all donors
            5: Quit
            >>> """).strip()
        if choice not in switch.keys():
            print(f'You input {choice}, please input 1 through 4')
        else:
            switch[choice](donor_collection)



if __name__=="__main__":
    while True:
        main()