class A:
    def __init__(self):
        print("A's init called")
        self.a = 54
        self.d = "set in a"
        print("type of self:", type(self))
        print("self.c:", self.c)

class B(A):
    def __init__(self):
        print("B's init called")
        self.b = 32
        self.d = "set in b"
        super().__init__()


class C(B):
    def __init__(self):
        print("C's init called")
        self.c = 15
        super().__init__()
    pass


# class D(B, C):
#     pass

