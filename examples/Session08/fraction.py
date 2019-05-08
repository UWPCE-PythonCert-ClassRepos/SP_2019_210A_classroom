import random
import time
import math


class Fraction:
    '''
    Simple class to represent fractions to be completed in class
    '''
    pass


if __name__ == '__main__':
    # f = Fraction(1, 0)  # ZeroDivisionError
    # f = Fraction(1.0, 2)    # TypeError
    f1 = Fraction(1, 2)
    print(f1)
    f2 = Fraction(2, 4)
    print(f1 == f2)     # True
    l = [Fraction(2, 3), Fraction(1, 2), Fraction(0, 1)]
    print(sorted(l))    # 0/1, 1/2, 2/3

    # sort key timing test
    N = 10000
    a_list = [Fraction(random.randint(0, 10000),
                       random.randint(1, 10000)) for _ in range(N)]
    # print("Before sorting:", a_list)

    print("Timing for {} items".format(N))
    start = time.clock()
    sorted(a_list)
    reg_time = time.clock() - start
    print("regular sort took: {:.4g}s".format(reg_time))

    start = time.clock()
    sorted(a_list, key=Fraction.sort_key)
    key_time = time.clock() - start
    print("key sort took: {:.4g}s".format(key_time))

    print("performance improvement factor: {:.4f}".format((reg_time / key_time)))

    # Add test
    print(Fraction(1, 3) + Fraction(1, 6))
