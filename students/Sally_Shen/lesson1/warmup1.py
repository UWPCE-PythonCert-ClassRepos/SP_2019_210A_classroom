def sleep_in(weekday, vacation):
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


def sum_double(a, b):
    if a == b:
        return (a+b)*2
    else:
        return a+b

def diff21(n):
    if n > 21:
        return (n-21)*2
    else:
        return 21-n


def parrot_trouble(talking, hour):
    if hour < 7 or hour > 20:
        return talking
    else:
        return False


def makes10(a, b):
    if a + b == 10:
        return True
    else:
        return a == 10 or b == 10

def near_hundred(n):
    return abs(n-100) <= 10 or abs(n-200) <= 10


def pos_neg(a, b, negative):
    if negative is True:
        return a < 0 and b < 0
    else:
        return a * b < 0



def not_string(str):
    if len(str) >= 3 and str[0:3] == 'not':
        return str
    else:
        return 'not '+str



def missing_char(str, n):
    if len(str) >= 0 and n >= 0 and n <= len(str) - 1:
        new_str = str[:n] + str[(n + 1):]
        return new_str
    else:
        return str



def front_back(str):
    if len(str) > 1:
        new_str = str[-1] + str[1:len(str)-1] + str[0]
        return new_str
    else:
        return str



def front3(str):
    if len(str) <= 3:
        new_str = str * 3
        return new_str
    else:
        new_str = str[:3] * 3
        return new_str
