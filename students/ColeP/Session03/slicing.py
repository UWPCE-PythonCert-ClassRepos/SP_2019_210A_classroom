# Write some functions that take a sequence as an argument, and return a copy of that sequence:

# with the first and last items exchanged.
# with every other item removed.
# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
# with the elements reversed (just with slicing).
# with the last third, then first third, then the middle third in the new order.

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def switch_first_last(seq):
    first = seq[0:1]
    last = seq[-1:]
    seq_mid = seq[1:-1]
    new_seq = last + seq_mid + first
    return new_seq


print(switch_first_last(a_string))
print(switch_first_last(a_tuple))


def every_other(seq):
    new_seq = seq[0::2]
    return new_seq


print(every_other(a_string))
print(every_other(a_tuple))


def first4_last4(seq):
    new_seq = seq[4:-4:2]
    return new_seq


print(first4_last4(a_string))
print(first4_last4(a_tuple))


def reverse_reverse(seq):
    new_seq = seq[::-1]
    return new_seq


print(reverse_reverse(a_string))
print(reverse_reverse(a_tuple))


def thirds(seq):
    first_third = seq[:(len(seq)//3)]
    middle_third = seq[len(seq)//3:-len(seq)//3]
    last_third = seq[-(len(seq)//3):]

    return last_third + first_third + middle_third


print(thirds(a_string))
print(thirds(a_tuple))

