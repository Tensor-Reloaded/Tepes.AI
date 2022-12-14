import csv
import glob
import os

from components.normalizer.converter import Convertor
from normalizer.filenormalizers.pdf_normalizer import PDFNormalizer
from normalizer.models.politician_model import PoliticianModel


class PoliticianConvertor(Convertor):
    def __init__(self):
        self.path = "..\\..\\crawler\\declarationscrawler\\data\\declarations"
        self.redirect_path = "..\\filenormalizers\\ocr_data"

    def cast_to_politician_and_save_csv(self):
        file_location = os.path.join(self.redirect_path, '*.pdf')
        filenames = glob.glob(file_location)
        politicians = []
        for file in filenames:
            pdf_normalizer = PDFNormalizer(file)
            last_name, first_name = pdf_normalizer.extract_name()
            functions = pdf_normalizer.extract_position()
            declaration_type = pdf_normalizer.extract_type_of_declaration()
            assets = pdf_normalizer.extract_assets()
            vehicles = pdf_normalizer.extract_vehicles()
            salary = pdf_normalizer.extract_salary()
            debt = pdf_normalizer.extract_debts()
            poltician = PoliticianModel(first_name, last_name, functions, declaration_type, 0, assets, vehicles, debt,
                                        salary)
            politicians.append(poltician)
        try:
            with open("csv_data\\politicians.csv", 'w', encoding="utf-8") as f:
                writer = csv.writer(f)
                for politician in politicians:
                    writer.writerow(
                        [politician.first_name, politician.last_name, politician.functions, politician.declaration_type,
                         0,
                         politician.assets, politician.vehicles, politician.debts, politician.salary])
        except BaseException:
            print('BaseException encountered!')
        else:
            print('Data has been loaded successfully!')


if __name__ == "__main__":
    politician_converter = PoliticianConvertor()
    politician_converter.cast_to_politician_and_save_csv()
