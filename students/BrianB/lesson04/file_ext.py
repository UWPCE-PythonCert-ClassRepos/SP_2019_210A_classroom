#! bin/usr/env python3

import os
import glob


def file_path():
    """
    finds python files and Returns their directory

    """

    for item in glob.glob('**.py'):
        print(os.path.abspath(item))
    return


def src_dst():
    """
    copies 'break_me.py' and moves it to an alternate directory

    """
    os.popen('cp ~/SP_2019_210A_classroom/students/BrianB/lesson01/break_me.py'
             '~/SP_2019_210A_classroom/students/BrianB/lesson04/break_me.py')
    return


def prog_langs():
    """
    reads "students.txt"

    returns: programming languages known by the students.

    """

    for line in open('students.txt'):
        for nickname_language in line.split(':'):
            for langauge in nickname_language.split():
                while True:
                    if langauge == langauge.lower():
                        print(langauge)
                    break


if __name__ == "__main__":
    #file_path()
    #src_dst()
    prog_langs()





