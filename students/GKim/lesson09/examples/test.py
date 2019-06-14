class A:
    def __init__(self):
        print("init A")

    def yo(self):
        print("yo A")

    def num(self, n):
        print("A", n)

class B(A):
    def __init__(self):
        print("init B")
        super().__init__()

    def yo(self):
        print("yo B")
        # super().yo()
        # A.yo(self)

    def num(self, n):
        print("B", n)
        super().num(n)


class C(A):
    def __init__(self):
        print("init C")
        super().__init__()

    def yo(self):
        print("yo C")
        # super().yo()
    def num(self, n):
        print("C", n)

    def only_c(self):
        print("only C")

class D(B,C):
    def __init__(self):
        print("init D")
        super().__init__()

    # def yo(self):
    #     print("yo D")
    #     # super().yo()
    #     B.yo(self)
    def num(self, n):
        print("D", n)
        # super().num(n)
        C.num(self, n)

d = D()
d.num(20)