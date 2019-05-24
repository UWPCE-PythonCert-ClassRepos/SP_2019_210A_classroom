
"""Practicing classes with car objects"""


class Car:
    def __init__(self, color, transmission_type, body_type, does_run):
        self.color = color
        self.transmission_type = transmission_type
        self.body_type = body_type
        self.does_run = does_run


    def move_car(self):
        if self.does_run == True:
            print("car is moving")
        else:
            print("fix the car")


    def use_clutch(self):
        if self.transmission_type == "Manual".lower():
            print("Press clutch to start the car")
        else:
            print("No clutch available")


c = Car("Red", "manual", "Hatch", False)
c.move_car()
c.use_clutch()


class Porsche(Car):
    def __init__(self, color, transmission_type, body_type, does_run, motor_type):
        super().__init__(color, transmission_type, body_type, does_run)
        self.motor_type = motor_type

    def motor_sound(self):
        if self.motor_type == "air cooled":
            print("Listen to the glorious air cooled sound!")
        else:
            print("The water cooled motor sound is great as well.")

    def define_porsche(self):
        print(f"The {self.color}, {self.motor_type} Porsches are some of the best cars you could possibly drive, when they run...")


p = Porsche("white", "manual", "911", True, "air cooled")
p.motor_sound()
p.define_porsche()


class DoMath():
    def multiply(self, x, y):
        return x * y


    def add_numbers(self, x, y):
        return x + y


    def subtract_stuff(self, x, y):
        return x - y

    def more_math(self, x, y):
        return (x + y) * 30


    def math_strings(self, x, y):
        i = x + y
        return f"The sum of {x} and {y} is equal to {i}"


    def print_results(self):
        print(self.multiply(10, 2))
        print(self.add_numbers(100, 100))
        print(self.subtract_stuff(2000, 13))
        print(self.more_math(100, 100))
        print(self.math_strings(10, 32))


do_math = DoMath()
do_math.print_results()