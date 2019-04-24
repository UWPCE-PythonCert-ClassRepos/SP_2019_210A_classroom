
#fizz_buzz.py
# write 1 to 100 inclusive
# for multiples of 3 print "Fizz"
# for multiples of 5 print "Buzz"


def fb():
    for i in range(100):
        fb_string = ""
        if i % 3 == 0:
            fb_string += 'Fizz'
        if i % 5 == 0:
            fb_string += 'Buzz'
        if len(fb_string) < 1:
            fb_string = str(i)
        print(fb_string)


fb()
