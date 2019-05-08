# super tests


class D:
    def __init__(self):
        print("D's called")
        super().__init__()

class A(D):
    def __init__(self):
        print("A's called")
        super().__init__()


class B(D):
    def __init__(self):
        print("B's called")
        super().__init__()


class C(B, A):
    def __init__(self):
        print("C's called")
        super().__init__()


