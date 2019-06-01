#! /usr/bin/env python3

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dog_details(self):
        print("{}=>{}".format(self.name, self.age))

    def run(self):
        print("run run run")

    def bark(self):
        print("bark bark")

    def poop(self):
        print("don't look at me")

    def sleep(self):
        print("zzzzzzzz")

class Chihuahua(Dog):
    def __init__(self, name, age, yappiness):
        super().__init__(name, age)
        self.yappiness = yappiness

    def dog_details(self):
        print("{}=>{} {}".format(self.name, self.age, self.yappiness))

    def run(self):
        print("prance prance prance")

    def bark(self):
        print("yip yip")


class Mastiff(Dog):
    def __init__(self, name, age, yappiness):
        super().__init__(name, age)
        self.yappiness = yappiness

    def dog_details(self):
        print("{}=>{} {}".format(self.name, self.age, self.yappiness))

    def run(self):
        print("clomp clomp")

    def bark(self):
        print("ruff ruff")