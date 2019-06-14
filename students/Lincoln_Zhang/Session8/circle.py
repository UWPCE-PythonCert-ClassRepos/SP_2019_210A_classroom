#!/usr/bin/env python3

class circle:
    #class attribute
    pi = 3.14

    #initiate a circle with a radius
    def __init__(self,value):
        self.radius = value

    #present instance radius
    def __repr__(self):
        return "A circle with radius {}".format(self.radius)
    
    #add two circles radius
    def __add__(self,other):
        print("add 2 circles radius")
        return self.radius + other.radius

    def __mul__(self,other):
        if isinstance(other,circle):
            print("circle A's radius multiplies circle B's radius")
            return self.radius * other.radius
        else:
            return self.radius * other or other * self.radius

    #make a list of instances sortable
    def __lt__(self,other):
        return self.radius < other.radius

    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return self.pi*(self.radius**2)

    #an alternatvie way to instantiate circle class    
    @classmethod
    def from_diameter(cls,value):
        self = cls(int(value/2))
        return self    

#inhertance of class circle
class sphere(circle):

    def __init__(self,value):
        super().__init__(value)

    def __repr__(self):
        return "A sphere with radius {}".format(self.radius) 

    @property    
    def volume(self):
        return 4/3*self.pi*(self.radius**3)

    @property
    def area(self):
        raise NotImplementedError
