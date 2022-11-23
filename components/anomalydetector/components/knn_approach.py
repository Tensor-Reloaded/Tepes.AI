import numpy as np
from pyod.models.knn import KNN
from pyod.utils import evaluate_print


class KnnApproach:
    @staticmethod
    def predict(salaries_df):
        salaries_df['class'] = 0

        salaries_df.at[11, 'class'] = 1
        salaries_df.at[86, 'class'] = 1
        salaries_df.at[549, 'class'] = 1
        salaries_df.at[912, 'class'] = 1

        X = salaries_df['Salary (in RON)'].values.reshape(-1, 1)
        y = salaries_df['class']

        clf = KNN(contamination=0.004, n_neighbors=6)
        clf.fit(X)

        y_train_pred = clf.labels_

        y_train_scores = clf.decision_scores_

        evaluate_print('KNN', y, y_train_scores)

        X_test_1 = np.array([[250.]])

        print("A salary of 250 will be considered: (0 - normal, 1 - abnormal)")
        print(clf.predict(X_test_1))

        print("A salary of 4200 will be considered: (0 - normal, 1 - abnormal)")
        X_test_2 = np.array([[4200.]])

        print(clf.predict(X_test_2))
