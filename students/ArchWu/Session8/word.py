class Tokenizer:
    def __init__(self, text):
        self.tokens = text.split()
    
    def describe(self):
        return self.tokens

class WordCounter(Tokenizer):
    def __init__(self, text):
        super().__init__(self, text)
        self.word_count = len(self.tokens)

    def describe(self):
        return self.word_count, self.tokens

class TextDescriber(WordCounter):
    def __init__(self, text):
        super().__init__(self, text)
        
