#!/usr/bin/env python


def test_data():

    donors = ["John Smith", "Ringo Eclipse", "Burt Syran", "Lance J. Johnson",
              "Orel Winfrey"]
    donations = [[25, 25], [25, 25, 25, 25], [50, 50, 50, 150], [25, 25, 50, 25], [500]]
    return dict(zip(donors, donations))

# The original version before refactoring.
# def create_donors_report(DONORS):
#     [name, total, number, avg] = [[], [], [], []]
#     for x in DONORS:
#         name.append(x)
#         total.append(sum(DONORS[x]))
#         number.append(len(DONORS[x]))
#         avg.append(total[-1] / number[-1])
#     donors_report = list(zip(name, total, number, avg))
#     donors_report = sorted(donors_report,
#                            key=lambda y: int(y[1]), reverse=True)
#     return donors_report


# the new version fully refactored:
def pack(don):
    n, don = don
    total = sum(don)
    return (n, total, len(don), (total / len(don)))


def create_donors_report(DONORS):
    donor_report = sorted([pack(don) for don in DONORS.items()],
                          key=lambda y: y[1], reverse=True)
    return donor_report

