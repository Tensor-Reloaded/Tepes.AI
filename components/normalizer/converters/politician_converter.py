from PyPDF2 import PdfFileReader
from components.Normalizer.converter import Convertor
import ocrmypdf
import os
import glob


class PoliticianConvertor(Convertor):
    def __init__(self):
        self.path = 'D:\Facultate\master anul 1\Tepes.AI\components\Crawler\declarationscrawler\data'

    def ocr_data(self):
        path = 'D:\Facultate\master anul 1\Tepes.AI\components\Crawler\declarationscrawler\data'
        file_location = os.path.join(path, 'declarations', '*.pdf')
        filenames = glob.glob(file_location)
        print(filenames)
        for declaration in filenames:
            with open(declaration, 'rb') as d:
                ocrmypdf.ocr(d, d)


if __name__ == "__main__":
    politician_converter = PoliticianConvertor()
    file_location = os.path.join(politician_converter.path, 'declarations', '*.pdf')
    print(file_location)
    filenames = glob.glob(file_location)
    print(filenames)
    for declaration in filenames:
        with open(declaration, 'r') as d:
            ocrmypdf.ocr(d, d)
