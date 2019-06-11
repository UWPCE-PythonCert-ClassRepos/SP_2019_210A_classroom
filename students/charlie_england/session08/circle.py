#!/usr/bin/env python
import math

class Circle:
    
    def __init__(self,radius):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    def __str__(self):
        return f"Circle of radius {self.radius}"

    def __add__(self,*args):
        total = self.radius
        for val in args:
            total += val.radius
        return total

    def __mul__(self,num):
        return self.radius*num

    def __gt__(self,circle2):
        return self.radius > circle2.radius

    def __lt__(self,circle2):
        return self.radius < circle2.radius

    @staticmethod 
    def something():
        return "this worked"#takes nothing as first param, basically is just assigned
    #not used much as it's just a regular function stuck into the same space
    #reason for static method, to keep stuff organized

    @classmethod
    def from_diameter(cls, diameter): #class method takes class as first param
        return cls(diameter/2) #DONT USE Circle here, use cls so when this is inherited it correctly assigns the correct class object

    @property #takes self as first param
    def diameter(self):
        return self.radius*2
    @property
    def area(self):
        return math.pi * self.radius**2

    @diameter.setter
    def diameter(self,diameter):
        self.radius = diameter/2
    # IF YOU WANT THE USER TO SET THE AREA :(
    # @area.setter
    # def area(self,area):
    #     self.radius = round(math.sqrt(self.area/math.pi),2)
    #     self.diameter = self.radius*2

class Sphere(Circle):
    
    @property
    def area(self):
        return 4*math.pi*self.radius**2

    @property
    def volume(self):
        return ((4/3)*math.pi*self.radius**3)
    
    def __repr__(self):
        return f"Sphere({self.radius})"

    def __str__(self):
        return f"Sphere of radius {self.radius}"