#  in class switch dictionary stuff

# def one():
#     return 'one'
#
#
# def main():
#
#     switch = {
#         '1': one,
#         '2': ...,
#         '3': ...,
#         '4': ...
#     }
#
#     while True:
#         choice = input('1-4')
#         if choice not in switch.keys():
#             print('select 1-4')
#         else:
#             switch[choice]()
donors_old = {"Donny Donor": [100, 10, 45],
          "Gav Giver": [12, 16, 20],
          "Stingy Steve": [2, 5, 1],
          "Freaky Frank": [1200, 999, 1005],
          }


class Donor:
    def __init__(self, name, donations=None):
        self.norm_name = self.normalize_name(name)
        self.name = name.strip()

        if donations is None:
            self.donations = []
        else:
            try:
                self.donations = list(donations)
            except:  # wants a specific error message?
                self.donations = [donations]

        # self.ty = '''
        # Dear {},
        #
        # Thank you for your most recent donation of ${:.2f} to The Org!
        #
        # -The Org'''.format(name, donations)

    def add_donation(self, donation):
        self.donations += [donation]

    def dictionize(self):
        return {self.name: self.donations}

    def ty(self):
        return ('''
        Dear {},

        Thank you for your most recent donation of ${:.2f} to The Org!

        -The Org'''.format(self.name, self.donations[-1]))

    @staticmethod
    def normalize_name(name):
        return name.lower().strip().replace(' ', '')


class StatsTable:
    def __init__(self, in_dict):
        self.in_dict = in_dict

    @staticmethod
    def header():
        return "{:22s} _ {:11s} _ {:9s} _ {:12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")

    @staticmethod
    def take_total(item):  # used in conjunction with sorted() to take the donations and sort by total donation
        return item[1]

    def body(self):
        compy = [(donor, sum(self.in_dict[donor]), len(self.in_dict[donor]),
                  sum(self.in_dict[donor]) / len(self.in_dict[donor])) for donor in self.in_dict]
        sorted_donors = sorted(compy, key=self.take_total, reverse=True)
        # sorts the donor list by their contribution totals

        empt = ''
        for row in sorted_donors:
            empt += ('{:22s} ${:11.2f} {:^13}$ {:>12.2f}\n'.format(*row))
        return empt

    def thx4all(self):
        for i in self.in_dict:
            with open('{}.txt'.format(i), 'w+') as let:
                let.writelines('''Dear {},

Thank you for your total donations of ${:.2f} to The Org!

-The Org'''.format(i, sum(self.in_dict[i])))

# class MakeDict:
#     def big_dict(*args):
#         d = {}
#         for i in args:
#             d = {**i}
#         return d


def main_menu():
    donors = {"Donny Donor": [100, 10, 45],
              "Gav Giver": [12, 16, 20],
              "Stingy Steve": [2, 5, 1],
              "Freaky Frank": [1200, 999, 1005],
              }
    while True:
        answer = input('''Choose an Option:
    1. Send a Thank You
    2. Create a Report
    3. Write Letters to all donors
    4. Quit 
    ''')

        answer = answer.strip()
        if answer == '1':  # maybe good
            ipt = input('Who would you like to thank?')

            if ipt in donors:
                lst_in = [int(input('How much did they give?'))]
                donors[ipt] += lst_in
            else:
                lst_in = [int(input('How much did they give?'))]
                a = {ipt: lst_in}
                donors = {**donors, **a}

            th = Donor(ipt, lst_in)
            print(th.ty())
        elif answer == '2':  # should be good
            re = StatsTable(donors)
            print(re.header())
            print(re.body())
        elif answer == '3':
            # letter to all
            l2a = StatsTable(donors)
            l2a.thx4all()
            print('Letters to donors with the sum of their donations sent out')
        elif answer == '4':
            break
            # quit_it()
        else:
            print('Please enter 1, 2, 3 or 4')


if __name__ == "__main__":
    print('Welcome to the Mailroom')

    main_menu()


class DonorCollection:
    def __init__(self, donors=None):
        if donors is None:
            self.donor_data = {}
        else:
            self.donor_data = {d.norm_name: d for d in donors}

# need:
# summary dictionary DONE
# thank you letter(s) DONE
# quit function
# main menu
#


'''
Donor makes a list of donations using self.donations

DonorCollection makes a set*?* of donor names 

use classes to organize the mailroom assignment
    maybe keep main_menu as a function that instantiates the other classes?
    

'''



