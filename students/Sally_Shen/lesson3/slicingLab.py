'''
Write some functions that take a sequence as an argument, and return a copy of that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.
'''


def exchange_first_last(seq):

    return seq[-1:] + seq[1:-1] + seq[:1]


print(exchange_first_last("this is a string"))


def every_other_removed(seq):
    return seq[::2]


print(every_other_removed("hello"))


def first4_last4_removed(seq):
    return seq[4:-4:2]


print(first4_last4_removed("hello world!"))


def reversed_elements(seq):
    return seq[::-1]


print(reversed_elements("hello world!"))


def new_order(seq):
    '''with the last third, then first third, then the middle third in the new order.
    first try:

    sep1 = int(len(seq) / 3)
    sep2 = int((len(seq) - sep1)/2)+sep1
    print(seq[sep2::] + seq[0:sep1] +seq[sep1:sep2])

    the code still works, depends on the requirements.
    '''


    sep1 = int(len(seq) / 3)
    return(seq[-sep1:] + seq[:-sep1])


print(new_order("this is a string"))

def main():
    a_string = "this is a string"
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_list) == [12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert every_other_removed(a_string) == "ti sasrn"
    assert every_other_removed(a_list) == [1, 3, 5, 7, 9, 11]
    assert every_other_removed(a_tuple) == (2, 13, 5)

    assert first4_last4_removed(a_string) == " sas"
    assert first4_last4_removed(a_list) == [5, 7]
    assert first4_last4_removed(a_tuple) == ( )

    assert reversed_elements(a_string) == "gnirts a si siht"
    assert reversed_elements(a_list) == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert reversed_elements(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert new_order(a_string) == "tringthis is a s"
    assert new_order(a_list) == [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8]
    assert new_order(a_tuple) == (5, 32, 2, 54, 13, 12)

    print("All assertions passed!")


if __name__ == '__main__':
    main()