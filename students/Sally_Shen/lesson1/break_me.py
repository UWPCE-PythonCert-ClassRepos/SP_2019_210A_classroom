
def TriggerNameError():
    print(doesNotExist)

TriggerNameError()



def TriggerTypeError():
    print(len(123))

TriggerTypeError()


def TriggerSyntaxError():
    import
    print('Hello World!')


class A:
    attr1: str
    attr2: int
    def __init__(self):
        self.attr2 = 123

def TriggerAttributeError():
    myA = A()
    print(myA.attr1)


TriggerAttributeError()
