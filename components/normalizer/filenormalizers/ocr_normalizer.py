from components.normalizer.normalizer_interface import NormalizerInterface
from PyPDF2 import PdfFileReader
import ocrmypdf


class OCRNormalizer(NormalizerInterface):
    def __init__(self, pdf_file):
        self.reader = PdfFileReader(pdf_file)

    def normalize_data(self):
        info = self.reader.getDocumentInfo()
        print(info)
        pages_number = self.reader.getNumPages()

        for p in range(pages_number):
            page = self.reader.getPage(p)
            print(page)
            print(p, page.extractText())


if __name__ == "__main__":
    file = r"/Users/razcro/PycharmProjects/TAIP-Facultate/components/crawler/declarationscrawler/data/declarations/declaratie_extract_ocr.pdf"
    new_file = r"/Users/razcro/PycharmProjects/TAIP-Facultate/components/crawler/declarationscrawler/data/declarations/declaratie_ocr_converter.pdf"

    ocrmypdf.ocr(file, new_file)
    with open (new_file, "rb") as f:
        pdf_normalizer = OCRNormalizer(f)
        pdf_normalizer.normalize_data()
