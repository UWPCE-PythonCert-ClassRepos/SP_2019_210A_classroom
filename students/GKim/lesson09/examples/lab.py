

class Athlete:
    def __init__(self, energy):
        self.energy = 100

    def display_energy(self):
        return self.energy

    
        
class Swimmer(Athlete):
    def __init__(self, energy):
        super().__init__(energy)

    def swim(self):
        print("I am swimming")
        self.energy -= 15
        print(self.energy)
        super().__init__()

class Runner(Athlete):
    def __init__(self, energy):
        super().__init__(energy)

    def run(self):
        print("I am running")
        self.energy -= 5
        print(self.energy)
        super().__init__()


class Cyclist(Athlete):
    def __init(self, energy):
        super().__init__(energy)

    def cycle(self):
        print("I am cycling")
        self.energy -= 10
        print(self.energy)
        super().__init__()

class Triathlete(Swimmer, Runner, Cyclist):
    def __init__(self, energy):
        super().__init__(energy)

    def action(self, swim, run, cycle):
        self.swim = -15
        self.run = -5
        self.cycle = -10

        print(self.energy)

a = Triathlete(100)
a.action()
