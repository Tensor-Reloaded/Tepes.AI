from components.contraction_fixer import ContractionFixer
from components.lemmatizer import Lemmatizer
from components.pos_tagger import POS_Tagger
from components.punctuation_remover import PunctuationRemover
from components.word_tokenizer import WordTokenizer

input_text = "It would be unfair to demand that people cease pirating files when " \
             "those same people aren't paid for their participation in very lucrative network schemes. " \
             "Ordinary people are relentlessly spied on, and not compensated for information taken from them. " \
             "While I'd like to see everyone eventually pay for music and the like, I'd not ask for it until there's " \
             "reciprocity."

text_without_contractions = ContractionFixer.fix(input_text)

text_tokenized = WordTokenizer.tokenize(text_without_contractions)

text_without_punctuation = PunctuationRemover.remove(text_tokenized)

text_with_base_words = Lemmatizer.lemmatize(text_without_punctuation)

print(text_with_base_words)

pos_tagged_word_list = POS_Tagger.tag(input_text)

print(pos_tagged_word_list)
