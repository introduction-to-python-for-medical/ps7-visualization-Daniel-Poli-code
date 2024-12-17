import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='diabetes', version=1, as_frame=True)

df = data.frame

features = list(df.columns)
print("Available features:", features)
selected_features = [features[0], features[2]]
print("Selected features: ", selected_features)
