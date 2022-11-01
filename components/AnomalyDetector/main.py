from components.AnomalyCreator import AnomalyCreator
from components.DataGenerator import DataGenerator
from components.KMeansApproach import KMeansApproach
from components.KnnApproach import KnnApproach

# We generate the data - 1000 people with salaries in 5 tiers - between 2500 and 35000
data = DataGenerator.generateData()

# We manually include some anomalies in the data - 3 salaries that are too small and one that is too large
data_with_anomalies = AnomalyCreator.createAnomalies(data)

# Clustering based approach - based on the salaries, we attempt to classify each salary based on
# value - thus, outliers can be clearly seen in the generated plot. We could potentially add many
# more labels and cluster based on them, or we could use the present approach as a guideline for
# versions of the Anomaly Detector to come
KMeansApproach.predict(data_with_anomalies)

# Classification problem based approach - based on the salaries and another label - that, in a real
# scenario, may be represented by a lot of things - if the person has been associated with known
# corrupted individuals, if he/she was, and many more
KnnApproach.predict(data_with_anomalies)
