#Slicing
#FredBallyns
#Session03


def exchange_first_last(seq):
    #Flips the fist and last
    return seq[-1:] + seq[1:-1] + seq[:1]


def every_other(seq):
    #Every other starting at zero
    return seq[::2]


def every_other_mid(seq):
    #Every other excluding first and last 4
    return seq[4:-4:2]


def reverse_order(seq):
    #Reverse order
    return seq[::-1]


def last_third_first(seq):
    #Moves last third to the front
    split = round(2/3*len(seq))
    return seq[split:]+seq[:split]





if __name__ == "__main__":
    # run a tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    print("exchange_first_last Works")

    assert every_other(a_string) == "ti sasrn"
    assert every_other(a_tuple) == (2, 13, 5)
    print("every_other Works")

    assert every_other_mid(a_string) == " sas"
    assert every_other_mid(a_tuple) == ()
    print("every_other_mid Works")


    assert reverse_order(a_string) == "gnirts a si siht"
    assert reverse_order(a_tuple) == (32, 5, 12, 13, 54, 2)
    print("reverse_order Works")

    a_string = "012345678"
    a_tuple = (0,1,2,3,4,5,6,7,8)
    assert last_third_first(a_string) == "678012345"
    assert last_third_first(a_tuple) == (6,7,8,0,1,2,3,4,5)
    print("last_third_first Works")