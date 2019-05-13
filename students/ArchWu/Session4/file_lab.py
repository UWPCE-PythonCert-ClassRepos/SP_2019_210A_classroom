import os
import sys
import re
from pathlib import Path

def task1():
    p = Path('.')
    for f in p.glob('*.*'):
        print(os.path.abspath(f))

def task2(filename):
    with open(filename, 'rb') as f:
        read_data = f.read()
    filetype = filename.split('.')[1]
    with open('new_file.{}'.format(filetype), 'wb') as f2:
        f2.write(read_data)

def read_n_parse():
    lang_stats = {}
    with open('students.txt') as f:
        read_data = f.readlines()
        for line in read_data:
            if line == 'Name: Nickname, languages\n':
                continue
            else:
                info = [x.strip() for x in line.split(':')]
                if info[1] is None:
                    print('Name: {}'.format(info[0]))
                else:
                    name = "Name: {} ".format(info[0])
                    languages = 'Languages:'
                    #nickname = 'Nickname: {}'.format(info[1].split(',')[0]) if info[1][0].isupper() else ''
                    #languages = 'Languages: {}'.format(info[1].split(',')) if info[1][0].isupper()
                    for lang in info[1].split(','):
                        #print(type(lang))
                        #print(list(lang))
                        if not lang:
                            #print('NOLANG')
                            continue
                        if lang[0].isupper():
                            nickname = 'Nickname: {} '.format(lang)
                            name = name + nickname
                        else:
                            if lang in lang_stats:
                                lang_stats[lang] += 1
                            else:
                                lang_stats[lang] = 1
                            language = "{}".format(lang)
                            languages = languages + language
                    result = name + languages
                    print(result)
        print(lang_stats)

if __name__ == '__main__':
    #task2('sherlock.txt')
    #task2('IVID0138.jpg')
    read_n_parse()
