# slicing
# first and last
seq = '3, 2, 1'
def exchange_first_last(seq):
    first = seq[-1]
    mid = seq[1:-1]
    last = seq[0]
    return print([first] + mid + [last])

# with every other item removed

my_list = "1, 2, 3, 4, 5, 6"
def remove_every_other(my_list):
    return my_list[::2]

# first four last four

def first_last_four(sequence):
    first_four = sequence[:4]
    last_four = sequence[-4:]
    new_sequence = first_four + last_four
    return new_sequence

# reversed

def elements_reversed(sequence):
    reverse_sequence = sequence[::-1]
    return reverse_sequence


# in thirds

def thirds(seq):
    result = seq[6:] + seq[:3] + seq[3:-3]
    return result

