from nltk.stem.wordnet import WordNetLemmatizer


class Lemmatizer:

    @staticmethod
    def lemmatize(input_text):
        return [WordNetLemmatizer().lemmatize(words_sent) for words_sent in input_text]
