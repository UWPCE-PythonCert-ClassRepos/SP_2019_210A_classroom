import sys
from donor_models import DonorCollection 

def do_thankyou(donor_collection):
    print("<<<SEND A THANK YOU>>>")

    donor_name, donation_amount = None, None
    
    while True:
        try:
            donor_name, donation_amount = get_donation(donor_collection)
        except Exception as e:
            print(e)
            continue
        break
                
    print_donors(donor_collection)
    print(f"Thank you {donor_name} for your generous donation amount of ${donation_amount}" )
    
def get_donation(donor_collection):
    donor_name = None
    while True:
        donor_name = input("Enter the name of donor or type 'list' if you wish to view the list of donors: ")
        if donor_name.lower() == 'list':
            print_donors(donor_collection)
        else:
            break
    
    donation_amount = input("Enter the donation amount: ")
    donor_collection.add_donation(donor_name, donation_amount)
    return donor_name, donation_amount

def print_donors(donor_collection):
    for donor in donor_collection.get_donors():
        print(donor.name + "\t" + str(donor.donations))
    
def do_createreport(donor_collection):
    print("<<<PRINTING REPORT>>>")
    sorted_donor = sorted(donor_collection.get_donors(), key=lambda donor: sum(donor.donations), reverse=True)
    print("{0:23}|  {1:15}|  {2:12}|  {3:10}".format('Donor Name','Total Given','Num Gifts', 'Average Gifts'))
    print('-' * 70)
    for donor in sorted_donor:
        stat = donor.get_stat()
        print("{0:18}      ${1:13}{2:15}     ${3:12}".format(donor.name, stat["Total"], stat["Count"], stat["Avg"]))
    print('-' * 70)

def do_sendlettertoalldonors(donor_collection):
    donor_collection.send_letter()
    print('Letters saved in your current directory with folder name starting with "Letters"')

def do_quit(donor_collection):
    print("--------Exit----------")
    sys.exit(0)
    
def main_menu():
    switch_func_dict = {
        '1': do_thankyou,
        '2': do_createreport,
        '3': do_sendlettertoalldonors,
        '4': do_quit
    }

    donor_collection = DonorCollection()
    
    while True:
        try:    
            answer = input("What would you like to do?\n"+
                           "Pick one:\n"+
                           "1: Send a Thank you\n"+
                           "2: Create a report\n"+
                           "3: Send letters\n"+
                           "4: Quit\n>>>")
            answer = answer.strip()
            option = switch_func_dict[answer]
        except:
            print("Incorrect option selected!")
            continue
        
        option(donor_collection)
        
if __name__ == "__main__":
    print("Welcome to mailroom!")
    main_menu()