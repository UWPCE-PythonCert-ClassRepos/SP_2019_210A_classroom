#! /usr/bin/env python3
import json

class Person:
    count = 0

    def __init__(self, perdict=[]):
        self.first_name = perdict['firstname']
        self.middle_name = perdict['middlename']
        self.last_name = perdict['lastname']
        self.age = int(perdict['age'])
        self.count += 1

    def __str__(self):
        return json.dumps({
            'firstname': self.first_name,
            'middlename': self.middle_name,
            'lastname': self.last_name,
            'age': self.age
        })

    def show_user(self):
        print("FN: {}".format(self.first_name))
        print("MN: {}".format(self.middle_name))
        print("LN: {}".format(self.last_name))
        print("AG: {}".format(self.age))
        print("CT: {}".format(self.count))


    """static methods is not bound to the object. its bound to the class
    and can be called against an uninitialized class"""
    @staticmethod
    def procreate(perdict=[]):
        return Person(perdict)


    """class method decorator"""

class Woman(Person):
    def __init__(self, perdict):
        super().__init__(perdict)
        self.gender = 'F'

    def show_user(self):
        print("FN: {}".format(self.first_name))
        print("MN: {}".format(self.middle_name))
        print("LN: {}".format(self.last_name))
        print("AG: {}".format(self.age))
        print("CT: {}".format(self.count))
        print("GE: {}".format(self.gender))
