a_string = "this is a string"
a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)


def first_last(string):
    a = string[:1]
    b = string[-1:]

    return (b + a)


def every_other(string):
    return string[::2]


def first4_last4(string):
    return string[4:-4:2]


def reverse(string):
    return string[::-1]


def third(string):
    c = int(len(string) / 3)
    beg = string[:c]
    end = string[-c:]
    mid = string[c:c + c]
    return end + beg + mid


print(first_last(a_string))
print(first_last(a_tuple))
print(every_other(a_string))
print(every_other(a_tuple))
print(first4_last4(a_string))
print(first4_last4(a_tuple))
print(reverse(a_string))
print(reverse(a_tuple))
print(third(a_string))
print(third(a_tuple))