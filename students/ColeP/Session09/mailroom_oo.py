
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
    def big_dict(*args):
        build = {}
        for arg in args:
            build.update(arg)
        return build

    @staticmethod
    def normalize_name(name):
        return name.lower().strip().replace(' ', '')

    @staticmethod
    def header():
        return "{:22s} _ {:11s} _ {:9s} _ {:12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")

    @staticmethod
    def take_total(item):  # used in conjunction with sorted() to take the donations and sort by total donation
        return item[1]

    def body(self, in_dict):
        compy = [(donor, sum(in_dict[donor]), len(in_dict[donor]),
                  sum(in_dict[donor]) / len(in_dict[donor])) for donor in in_dict]
        sorted_donors = sorted(compy, key=self.take_total, reverse=True)
        # sorts the donor list by their contribution totals

        empt = ''
        for row in sorted_donors:
            empt += ('{:22s} ${:11.2f} {:^13}$ {:>12.2f}\n'.format(*row))
        return empt

    def thx4all(self, in_dict2):
        for i in in_dict2:
            with open('{}.txt'.format(i), 'w+') as let:
                let.writelines('''Dear {},

Thank you for your total donations of ${:.2f} to The Org!

-The Org'''.format(i, sum(in_dict2[i])))


def main_menu():
    # donors = {"Donny Donor": [100, 10, 45],
    #           "Gav Giver": [12, 16, 20],
    #           "Stingy Steve": [2, 5, 1],
    #           "Freaky Frank": [1200, 999, 1005],
    #           }

    a = Donor('Marg Marty', 122)
    a.add_donation(55)
    a.add_donation(94)
    b = Donor('Cole Phalen')
    b.add_donation(12)
    b.add_donation(33)
    b.add_donation(101)
    c = Donor('Mikey', 69)
    c.add_donation(17)
    c.add_donation(50)

    donors = a.big_dict(a.dictionize(), b.dictionize(), c.dictionize())

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
                new_don = {ipt: lst_in}
                donors = {**donors, **new_don}

            th = Donor(ipt, lst_in)
            print(th.ty())

        elif answer == '2':  # creates report
            # re = StatsTable(donors)
            print(a.header())
            print(a.body(donors))

        elif answer == '3':  # writes letter to all donors
            # letter to all
            # l2a = StatsTable(donors)
            a.thx4all(donors)
            print('Letters to donors with the sum of their donations sent out')
        elif answer == '4':
            break
            # quit_it()
        else:
            print('Please enter 1, 2, 3 or 4')


# def main_menu2():
#     # unsure if my first idea of main_menu is what was asked for
#     # so i tried to make another with slightly different execution
#
#     # init_ipt = input('Who is our first donor?')
#
#     donors = {}
#
#     while True:
#         answer = input('''Choose an Option:
#     1. Send a Thank You
#     2. Create a Report
#     3. Write Letters to all donors
#     4. Quit
#     ''')
#
#         answer = answer.strip()
#         if answer == '1':  # maybe good
#             ipt = input('Who would you like to thank?')
#             a = Donor(ipt)
#             b = Donor(ipt)
#             donors = a.big_dict(b.dictionize())
#
#             if ipt in donors:
#                 lst_in = int(input('How much did they give?'))
#                 don = {ipt: [lst_in]}
#                 donors = {**donors, **don}
#
#             else:
#                 lst_in = [int(input('How much did they give?'))]
#                 b = Donor(ipt, lst_in)
#                 # new_don = {ipt: lst_in}
#                 donors = {**donors, **b.dictionize()}
#
#             th = Donor(ipt, lst_in)
#             print(th.ty())
#
#         elif answer == '2':  # creates report
#             # try, except with error from a.header, please 'send thank u' to add new donor
#             print(a.header())
#             print(a.body(donors))
#
#         elif answer == '3':  # writes letter to all donors
#             # letter to all
#             # l2a = StatsTable(donors)
#             a.thx4all(donors)
#             print('Letters to donors with the sum of their donations sent out')
#         elif answer == '4':
#             break
#             # quit_it()
#         else:
#             print('Please enter 1, 2, 3 or 4')


if __name__ == "__main__":
    print('Welcome to the Mailroom')

    main_menu()


# class DonorCollection:
#     def __init__(self, donors=None):
#         if donors is None:
#             self.donor_data = {}
#         else:
#             self.donor_data = {d.norm_name: d for d in donors}

