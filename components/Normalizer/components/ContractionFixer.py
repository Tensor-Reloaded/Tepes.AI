import contractions


class ContractionFixer:
    @staticmethod
    def fix(input_text):
        return contractions.fix(input_text)

