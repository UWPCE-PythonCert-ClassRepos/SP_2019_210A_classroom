class Devices:
    def __init__(self, name):
        self.name = name
    

class Phones(Devices):
    def __init__(self, name):
        super().__init__(name)
        self.contacts = []
    
    def call(self, callee):
        print('making a phone call to {}'.format(callee))
    
    def save(self, name, number):
        if not self.check(name):
            self.contacts.append((name,number))
    
    def check(self, name):
        if name in self.contacts:
            print("Already in contacts")
            return True
        else:
            return False

class Camera(Devices):
    def __init__(self, name):
        super().__init__(name)
    
    def take_pic(self):
        return None

    
