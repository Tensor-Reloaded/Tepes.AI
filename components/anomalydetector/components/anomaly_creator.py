import matplotlib.pyplot as plt


class AnomalyCreator:
    @staticmethod
    def createAnomalies(salaries_df):
        salaries_df.at[11, 'Salary (in RON)'] = 1650
        salaries_df.at[86, 'Salary (in RON)'] = 1900
        salaries_df.at[549, 'Salary (in RON)'] = 0
        salaries_df.at[912, 'Salary (in RON)'] = 50000
        salaries_df['Salary (in RON)'].plot(kind='box')
        plt.show()
        ax = salaries_df['Salary (in RON)'].plot(kind='hist')
        ax.set_xlabel('Salary (in RON)')
        plt.show()
        return salaries_df
