import glob
import os

import ocrmypdf
from PyPDF2 import PdfFileReader

from components.normalizer.normalizer_interface import NormalizerInterface
from normalizer.converters.politician_converter import PoliticianConvertor


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
    politician_converter = PoliticianConvertor()
    file_location = os.path.join(politician_converter.path, '*.pdf')
    filenames = glob.glob(file_location)
    for file in filenames:
        ocrmypdf.ocr(file, file.replace(".pdf", "_ocr.pdf").replace(politician_converter.path,
                                                                    politician_converter.redirect_path))
