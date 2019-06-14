#! /usr/bin/env python3


class Tokenizer:
    """Tokenizes the text"""
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

    def describe(self):
        return self.tokens, self.word_count, self.vocab