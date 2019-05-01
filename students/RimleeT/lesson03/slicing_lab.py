"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:
with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.
"""

# Exchange first and last item
def exchange_first_last(seq):
	if len(seq)<=1:
		return seq
	else:
		a_new_sequence = seq[-1]+ seq[1:len(seq)-1] + seq[0]
		return a_new_sequence
	
assert exchange_first_last("this is a string") == "ghis is a strint"
assert exchange_first_last("w") == "w"

# Keep first and last items with other items removed. 
def only_first_last(seq):
    if len(seq)<=1:
        return(seq)
    else:
        a_new_sequence = seq[0]+seq[-1]
        return(a_new_sequence)

assert only_first_last("this is a string") == "tg"
assert only_first_last("w") == "w"

#first 4 and the last 4 items removed
def first_and_last_four_removed (seq):
	if len(seq)<=8:
		#print(seq)
		return(seq)
	else:
		a_new_sequence = seq[4:]
		a_new_sequence = a_new_sequence[:-4]
		#print(a_new_sequence)
		return(a_new_sequence)
		
assert first_and_last_four_removed("this is a string") == " is a st"
assert first_and_last_four_removed("w") == "w"
assert first_and_last_four_removed("abcd") == "abcd"

#elements reversed
def elements_reversed (seq):
	if len(seq)<=1:
		return(seq)
	else:
		a_new_sequence = seq[ : :-1]
		return (a_new_sequence)
		
assert elements_reversed("this") == "siht"
assert elements_reversed("w") == "w"
assert elements_reversed("ab") == "ba"

#with the last third, then first third, then the middle third in the new order
def find_third (seq):
	if len(seq) < 3:
		#print("String contains less than 3 items")
		return("String contains less than 3 items")
	elif len(seq) == 3:
		return(seq[-1])
	else:
		a_new_sequence = seq[-3]
		if len(seq)-3 < 3:
			a_new_sequence = seq[-3]
		elif len(seq)-3 == 3:
			a_new_sequence = seq[-3]+seq[2]
		else:
			a_middle_string = seq[3:-4]
			if len(a_middle_string) < 3:
				a_new_sequence = seq[-3]+seq[2]
			else:
				a_middle_item = a_middle_string[2]
				a_new_sequence = seq[-3]+seq[2]+a_middle_item	
		#print(a_new_sequence)				
		return(a_new_sequence)

assert find_third("this") == "h"
assert find_third("w") == "String contains less than 3 items"
assert find_third("abc") == "c"
assert find_third("reverse") == "rv"
assert find_third("This is a string") == "iii"
assert find_third("this") == "h"
assert find_third("thisw") == "i"
assert find_third("thiswe") == "si"
assert find_third("thiswer") == "wi"
assert find_third("reversemylist") == "ivs"

