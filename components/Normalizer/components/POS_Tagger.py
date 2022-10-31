from nltk.tokenize import word_tokenize
import nltk


class POS_Tagger:
    @staticmethod
    def tag(input_text):
        return nltk.pos_tag(nltk.word_tokenize(input_text))
