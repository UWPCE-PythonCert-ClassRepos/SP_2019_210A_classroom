import random
bevy = ['wine', 'water', 'la croix', 'popcorn']


class Dogs:

    def __init__(self, color, size, fur, tail):
        self.color = color
        self.size = size
        self.fur = fur
        self.tail = tail

    def bark(self):
        if self.size == 'medium':
            return'bark'
        elif self.size == 'large':
            return'BARK!'

    def spill(self):
        if self.tail:
            return 'spilled the {}'.format(random.choice(bevy))


Tazu = Dogs('black tri', 'medium', 'long hair', None)
Lucy = Dogs('black', 'large', 'short fur', True)

print(Tazu.size)
print(Lucy.size)

print(Tazu.bark())
print(Lucy.bark())

print(Tazu.spill())
print(Lucy.spill())
