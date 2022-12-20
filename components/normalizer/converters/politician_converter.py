import csv
import glob
import os

import pandas as pd
from pythonrv import rv

from components.normalizer.converter import Convertor
from components.normalizer.filenormalizers.pdf_normalizer import PDFNormalizer
from components.normalizer.models.politician_model import PoliticianModel


class PoliticianConvertor(Convertor):
    def __init__(self):
        self.path = "..\\..\\crawler\\declarationscrawler\\data\\declarations"
        self.redirect_path = "..\\filenormalizers\\ocr_data"
        self.csv_path = "csv_data\\politicians.csv"

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
            with open(self.csv_path, 'w', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["first_name", "last_name", "functions", "declaration_type",
                                 "investments",
                                 "assets", "vehicles", "debts", "salary"])
                for politician in politicians:
                    writer.writerow(
                        [politician.first_name, politician.last_name, politician.functions, politician.declaration_type,
                         0,
                         politician.assets, politician.vehicles, politician.debts, politician.salary])
        except BaseException:
            print('BaseException encountered!')
        else:
            print('Data has been loaded successfully!')


def clean_csv_rows(csv_path):
    csv = pd.read_csv(csv_path)
    csv = csv[csv['salary'].notnull()]
    return csv
    # TODO: ADD MORE SANITIZATION FUNCTIONALITY ONCE THE APPLICATION SCALES


def validate(csv_path):
    csv = pd.read_csv(csv_path)
    rows = ["first_name", "last_name", "functions", "declaration_type",
            "investments",
            "assets", "vehicles", "debts", "salary"]
    if set(rows) != set(csv.columns):
        return False
    return True
    # TODO: ADD MORE VALIDATION ONCE THE APPLICATION SCALES


# @rv.monitor(validate=validate, clean=clean_csv_rows)
# @rv.spec(when=rv.PRE, history_size=3)
def validate_then_send(event):
    if event.fn.validate.called:
        print("Validation was conducted!")
    elif event.fn.clean.called:
        if event.history[0].called_function != event.history[0].fn.validate:
            print("Invalid order! Validation should be conducted before cleaning!")
        else:
            print("Cleaning was conducted!")


def print_dataframe(csv_path):
    validate(csv_path)
    csv = clean_csv_rows(csv_path)
    print(csv)


if __name__ == "__main__":
    politician_converter = PoliticianConvertor()
    politician_converter.cast_to_politician_and_save_csv()
    print_dataframe("csv_data\\politicians.csv")
