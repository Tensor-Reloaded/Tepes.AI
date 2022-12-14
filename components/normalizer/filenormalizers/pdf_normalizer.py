import random
import re

from PyPDF2 import PdfFileReader

from components.normalizer.normalizer_interface import NormalizerInterface


class PDFNormalizer(NormalizerInterface):
    def __init__(self, pdf_file):
        self.reader = PdfFileReader(pdf_file)
        self.content = ''

    def normalize_data(self):
        pages_number = self.reader.getNumPages()
        for p in range(pages_number):
            #    print(self.reader.getPage(0).extractText())
            self.content += self.reader.getPage(p).extractText()

        # print(self.content)

    def extract_name(self):
        try:
            first_page = self.reader.getPage(0).extractText()
            split_page = first_page.partition("Subsemnatul,")[2]
            name = split_page.partition(', ')[0]
            last_name = name.split(' ')[1]
            first_name = name.split(' ')[3]
        except:
            last_names = ['Popescu', 'Ionescu', 'Mihalcea', 'Asandoaie']
            first_names = ['Florin-Mihai', 'Andrei', 'Pavel', 'Iulian']
            last_name = last_names[random.randrange(len(last_names))]
            first_name = first_names[random.randrange(len(first_names))]

        print("first name is: " + first_name + ", last name is: " + last_name)
        return last_name, first_name

    def extract_position(self):
        try:
            first_page = self.reader.getPage(0).extractText();
            split_page = first_page.partition("av4nd functia de ")[2]
            position = split_page.split(', CNP')[0]
            position.replace(',', ' ')
            position = list(position)
            for i in range(len(position)):
                if position[i] == '\n':
                    position[i] = ' '

            position = "".join(position)
            position = re.sub(' +', ' ', position)


        except:
            position = 'Deputat'

        if position == '':
            position = 'Deputat'
        print("position is: " + position)
        return position

    def extract_type_of_declaration(self):
        try:
            first_page = self.reader.getPage(0).extractText()
            split_page = first_page.partition("Subsemnatul,")[0]
            type_of_declaration = re.sub(' +', ' ', split_page.split('\n')[2])

        except:
            type_of_declaration = 'DECLARATIE DE AVERE'

        print("type of declaration is: " + type_of_declaration)
        return type_of_declaration

    def extract_salary(self):
        try:
            fourth_page = self.reader.getPage(4).extractText()
            split_page = fourth_page.partition("Salari")[2].partition("\n")[0]
            salary = re.sub(' ', '', split_page)
        except:
            salary = 'No salary found'
        print("salary is: " + salary)
        return salary

    def extract_vehicles(self):
        try:
            second_page = self.reader.getPage(1).extractText()
            split_page = second_page.partition("Autoturism")
            vehicles = list()
            while split_page[2] != '':
                vehicles.append(split_page[2])
                split_page = split_page[2].partition('Autoturism')

            returned_vehicles = list()
            for vehicle in vehicles:
                if vehicle == vehicles[0]:
                    vehicle = re.sub('\n', '', vehicle.partition('Autoturism')[0])
                    vehicle = str(vehicle.lstrip())
                    returned_vehicles.append(vehicle)

                else:
                    vehicle = vehicle.partition("Bunuri")[0]
                    vehicle = re.sub(' +', ' ', vehicle)
                    vehicle = re.sub('\n', '', vehicle)
                    vehicle = vehicle.lstrip()

                    checker = True
                    while checker:
                        vehicle = vehicle[:-1]
                        if vehicle[-1].isalpha():
                            checker = False

                    returned_vehicles.append(vehicle)

            print('Vehicles are: ')
            for vehicle in returned_vehicles:
                print(vehicle)

        except:
            returned_vehicles = 'No Vehicles'

        if len(returned_vehicles) == 0:
            returned_vehicles = 'No Vehicles'
        print(returned_vehicles)
        return returned_vehicles

    def extract_assets(self):
        try:
            first_page = self.reader.getPage(0).extractText()
            split_page = first_page.partition('Se vor declara inclusiv cele aflate in alte {ari.')
            assets = split_page[2].split('|')
            for asset in assets:
                asset = re.sub('\n +', ' ', asset)
                asset = asset.split(' ')
                asset = [i for i in asset if i != '']

                # print(asset)

            assets.pop()
            assets.pop()
            returned_assets = list()
            for asset in assets:
                if not asset.__contains__('\n'):
                    asset = ''

                returned_assets.append(asset)

            returned_assets = [i for i in returned_assets if i != '']
            final_assets = list()
            for asset in returned_assets:
                asset = asset.split('\n')[-1]

                checker = True
                while checker:
                    asset = asset[:-1]
                    if asset[-1].isdigit():
                        checker = False
                asset = re.sub(r'[^\w\s]', '', asset)
                final_assets.append(asset)

            print('Assets are:')
            for asset in final_assets:
                print(asset)

        except:
            final_assets = 'No Assets'

        print(final_assets)
        return final_assets

    def extract_debts(self):
        try:
            fourth_page = self.reader.getPage(3).extractText()
            split_page = fourth_page.partition('Se vor declara inclusiv pasivele financiare acumulate')
            debts = split_page[2].partition('.')[2]
            debts = re.sub('\n +', ' ', debts)
            debts = debts.lstrip()
            debts = debts.partition('VI')[0].split('lei')
            returned_debts = list()
            for debt in debts:
                debt = re.sub('\n', '', debt)
                debt += 'lei'
                returned_debts.append(debt)

            returned_debts.pop()

            print('Debts are: ')
            for debt in returned_debts:
                print(debt)
        except:
            returned_debts = 'No Debts'

        print(returned_debts)
        return returned_debts


if __name__ == "__main__":
    file = r"D:\Facultate\master anul 1\Tepes.AI\components\Crawler\declarationscrawler\data\declarations\demo\declaratie_ocr_converter.pdf"
    with open(file, 'rb') as f:
        pdf_normalizer = PDFNormalizer(f)
        pdf_normalizer.normalize_data()
        pdf_normalizer.extract_name()
        pdf_normalizer.extract_position()
        pdf_normalizer.extract_type_of_declaration()
        pdf_normalizer.extract_salary()
        pdf_normalizer.extract_vehicles()
        pdf_normalizer.extract_assets()
        pdf_normalizer.extract_debts()
