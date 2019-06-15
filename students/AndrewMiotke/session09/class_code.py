# Example 1

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



# ---------------------------------------------------------------------
# Example 2
# Word tokenizer

class Tokenizer:

    def __init__(self, text):
        self.tokens = text.split()


    def describe(self):
        return self.tokens


class WordCounter(Tokenizer):
    def __init__(self, text):
        super().__init__(text)
        self.word_count = len(self.tokens)


    def describe(self):
        return self.tokens, self.word_count


class Vocabulary(Tokenizer):
    def __init__(self, text):
        super().__init__(text)
        self.vocab = set(self.tokens)


    def describe(self):
        return self.tokens, self.vocab


class TextDescriber(WordCounter, Vocabulary):
    def __init__(self, text):
        super().__init__(text)
        """
        Inheriting Classes:
         - WordCount
         - Tokenizer
         - Vocabulary
         """

    def describe(self):
        return self.tokens, self.word_count, self.vocab


# ---------------------------------------------------------------------
# Example 3
# Peagesus

class Horse():
    def __init__(self, color):
        self.color = color


    def get_color(self, color):
        color = input("What color is it? ")
        return color


class Bird():
    def __init__(self, beak):
        self.beak = beak


    def has_beak(self):
        self.beak = False



class Peagesus(Horse, Bird):
    def __init__(self, name, color):
        super().__init__(color)


    def get_name(self, name):
        ask_for_name = input("What's the name of this thing? ")
        return ask_for_name


    def print_peagesus(self):
        return self.get_name, self.color, self.has_beak


# ---------------------------------------------------------------------
# Example 4
# Audi RS2

class Audi():

    def body(self):
        audi = "Audi"

        print(f"The body was designed by {audi}")


class Porsche():

    def motor(self):
        porsche = "Porsche"

        print(f"The motor was designed by {porsche}")


class RS2(Audi, Porsche):
    def __init__(self):
        super().__init__()


    def print_car(self):
        print(f"{self.motor()} {self.body()}")

# ---------------------------------------------------------------------

# add all numbers in the list
sum([1, 3, 5])

# Combine list of strings
len("".join(["ksljlkdjf", "asdkjl", "llkj"]))