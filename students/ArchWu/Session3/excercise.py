def exchange_first_last(seq):
    if type(seq) == tuple:
        a = []
        a.append(seq[-1])
        b = list(seq[1:-1])
        c = []
        c.append(seq[0])

        a_new_sequence = a + b + c
        return tuple(a_new_sequence)
    else:
        a_new_sequence = seq[-1] + seq[1:-1] + seq[0]
    return a_new_sequence
