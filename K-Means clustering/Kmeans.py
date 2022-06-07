from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
import numpy as np
dataset= pd.read_csv('/content/drive/MyDrive/data set csp201/mall_customers.csv')
dataset.head()
import matplotlib.pyplot as plt
X = dataset.iloc[:, [3,4]].values  
X
from sklearn.cluster import KMeans  

kmeans = KMeans(n_clusters=5, init='k-means++', random_state= 48)  
pred= kmeans.fit_predict(x)  
plt.figure(figsize=(10,6))
plt.scatter(X[pred == 0, 0], X[pred == 0, 1], c = 'brown', label = 'Cluster 0')
plt.scatter(X[pred == 1, 0], X[pred == 1, 1], c = 'green', label = 'Cluster 1')
plt.scatter(X[pred == 2, 0], X[pred == 2, 1], c = 'blue', label = 'Cluster 2')
plt.scatter(X[pred == 3, 0], X[pred == 3, 1], c = 'purple', label = 'Cluster 3')
plt.scatter(X[pred == 4, 0], X[pred == 4, 1], c = 'orange', label = 'Cluster 4')

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:, 1],s = 300, c = 'red', label = 'Centroid', marker='*')

plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.title('Customer Clusters')

