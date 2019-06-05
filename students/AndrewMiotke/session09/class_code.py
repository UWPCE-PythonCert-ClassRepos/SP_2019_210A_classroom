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