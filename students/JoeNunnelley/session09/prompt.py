#! /usr/bin/env python3

class Man:
    def __init__(self):
        print('Man')

    def noise(self):
        print('Hi!')

class Bear(Man):
    def __init__(self):
        print('Bear')
        super().__init__()

    def noise(self):
        print('Roar!')
        super().noise()

class Pig(Man):
    def __init__(self):
        print('Pig')
        super().__init__()

    def noise(self):
        print('Oink!')
        super().noise()


class ManBearPig(Pig, Bear):
    def __init__(self):
        super().__init__()

    def noise(self):
        super().noise()

