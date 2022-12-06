from components.Normalizer.normalizer_interface import NormalizerInterface
from PyPDF2 import PdfFileReader


class PDFNormalizer(NormalizerInterface):
    def __init__(self, pdf_file):
        self.reader = PdfFileReader(pdf_file)

    def normalize_data(self):
        info = self.reader.getDocumentInfo()
        print(info)
        pages_number = self.reader.getNumPages()

        for p in range(pages_number):
            page = self.reader.getPage(p)
            # print(page)
            # print(p, page.extractText())

    def extract_name(self):
        first_page = self.reader.getPage(0).extractText();
        split_page = first_page.partition("Subsemnatul,")[2];
        # print(split_page)
        name = split_page.partition(', ')[0]
        last_name = name.split(' ')[1]
        first_name = name.split(' ')[3]
        print("first name is: " + first_name + ", last name is: " + last_name)
        return last_name, first_name

    def extract_position(self):
        first_page = self.reader.getPage(0).extractText();
        split_page = first_page.partition("av4nd functia de ")[2];
        position = split_page.split(', CNP')[0]
        print(split_page.split(', CNP'))
        print("position is: " + position)
        position.replace(',', ' ')
        print(position)
        return position

if __name__ == "__main__":
    file = r"D:\Facultate\master anul 1\Tepes.AI\components\Crawler\declarationscrawler\data\declarations\declaratie_ocr_converter.pdf"
    with open(file, 'rb') as f:
        pdf_normalizer = PDFNormalizer(f)
        pdf_normalizer.normalize_data()
        pdf_normalizer.extract_name()
        pdf_normalizer.extract_position()
