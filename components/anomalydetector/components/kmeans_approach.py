import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.vq
from scipy.cluster.vq import kmeans


class KMeansApproach:
    @staticmethod
    def predict(salaries_df):
        salaries_raw = salaries_df['Salary (in RON)'].values

        salaries_raw = salaries_raw.reshape(-1, 1)
        salaries_raw = salaries_raw.astype('float64')

        # Salaries ranging from 2000 - 5000, 5000 - 8000, 8000 - 15000, 15000 - 25000, 25000 - 35000
        centroids, avg_distance = kmeans(salaries_raw, 5)
        groups, c_distance = scipy.cluster.vq.vq(salaries_raw, centroids)

        plt.scatter(salaries_raw, np.arange(0, 1000), c=groups)
        plt.xlabel('Salaries (in RON)')
        plt.ylabel('Indices')
        plt.show()
