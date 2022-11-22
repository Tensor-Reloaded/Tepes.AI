import numpy as np
import pandas as pd
from faker import Faker


class DataGenerator:
    @staticmethod
    def generateData():
        fake = Faker()

        person_name_list = []
        salaries = []

        for _ in range(1000):
            person_name_list.append(fake.name())
            salaries.append(np.random.randint(2500, 35000))

        return pd.DataFrame({
            'Person': person_name_list,
            'Salary (in RON)': salaries
        })
