class A:
    def __init__(self):
        print("In class A")


    def yo(self):
        pass


    def num(self, n):
        print("A", n)


class B(A):
    def __init__(self):
        print("In class B")
        super().__init__()


    def yo(self):
        print("yo B")
        # super().yo()


    def num(self, n):
        print("B", n)


class C(A):
    def __init__(self):
        print("In class C")
        super().__init__()


    def yo(self):
        print("Yo C")
        # super().yo()


    def num(self, n):
        print("C", n)


class D(B, C):
    def __init__(self):
        print("In class D")
        super().__init__()


    def yo(self):
        print("Yo D")
        # super().yo()

    def num(self, n):
        print("D", n)
        super().num(n)

