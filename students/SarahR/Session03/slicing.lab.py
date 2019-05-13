#!/usr/bin/env python3


# Write some functions that take a sequence as an argument, and return a copy of that sequence:

# with the first and last items exchanged.
# with every other item removed.
# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
# with the elements reversed (just with slicing).
# with the last third, then first third, then the middle third in the new order.

seq = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]


# with the first and last items exchanged.
def seq_inverted(seq):
    seqInverted = [seq[-1], seq[1:-1], seq[0]]
    print(seqInverted)

    return seqInverted

# with every other item removed.
def seq_every_other_rem(seq):

    seqEveryOtherRem = seq[slice(0, -1, 2)]
    print(seqEveryOtherRem)
    return seqEveryOtherRem

# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def seq_removed(seq):

    seqRemoved = seq[slice(4, -4, 2)]
    print(seqRemoved)
    return seqRemoved

# with the elements reversed (just with slicing).
def seqReversed(seq):

    seqReversed = seq[::-1]

    print(seqReversed)

# with the last third, then first third, then the middle third in the new order.
#setThirds =

seq_inverted(seq)
seq_every_other_rem(seq)
seq_removed(seq)
seqReversed(seq)