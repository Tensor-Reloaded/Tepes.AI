class PunctuationRemover:
    @staticmethod
    def remove(token):
        return [word for word in token if word.isalpha()]
