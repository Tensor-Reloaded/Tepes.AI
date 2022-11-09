from nltk.tokenize import word_tokenize


class WordTokenizer:
    @staticmethod
    def tokenize(input_text):
        return word_tokenize(input_text)
