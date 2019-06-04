
test_string = "this is my chosen test string."
test_tuple = ("thing 1", "thing 2", 54, 40.1, "last thing")
test_list = [12, 45, 31, 12, 56, 88, 97, 4, 23, 63, 34, 90]


def string_repeat(str):
    print("test 1: ",str)


def first_and_last_swap(str):
    print("test 2: ",str[-1:], str[1:-1], str[0:1])


def four_removed_alternate(str):
    print("test 3: ", str[5:-4:2])


def string_reversed(str):
    print("test 4: ", str[::-1])


def string_thirds(str):
    str_len = len(str)
    thirds = int(str_len / 3)
    two_thirds = thirds * 2
    print("test 5: ", str[two_thirds:], str[0:thirds], str[thirds:two_thirds])

string_repeat(test_string)
first_and_last_swap(test_string)
four_removed_alternate(test_string)
string_reversed(test_string)
string_thirds(test_string)

string_repeat(test_tuple)
first_and_last_swap(test_tuple)
four_removed_alternate(test_tuple)
string_reversed(test_tuple)
string_thirds(test_tuple)

string_repeat(test_list)
first_and_last_swap(test_list)
four_removed_alternate(test_list)
string_reversed(test_list)
string_thirds(test_list)