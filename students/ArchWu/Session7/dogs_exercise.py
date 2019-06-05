class Dog:
    def __init__(self, color, birthdate, f_f):
        self.color = color
        self.birthdate = birthdate
        self.f_f = f_f

    def sit():
        pass

    def run():
        pass


    def eat():
        pass



class Corki(Dog):
    breed = 'Corki'

    def __init__(self, color, birthdate, f_f):
        super().__init__(color, birthdate, f_f)

    def sit():
        super().sit()

    def run():
        super().run()

    def eat():
        super().eat()

    def bark():
        print('woof')

class GoldenRetriv(Dog):
    breed = 'Golden Retriver'
