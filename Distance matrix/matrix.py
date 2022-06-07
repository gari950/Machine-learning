from google.colab import drive
import pandas as pd
drive.mount('/content/drive')
dataset= pd.read_csv('/content/drive/MyDrive/data set csp201/flats_moscow.csv')
dataset.head()
import numpy as np
x=dataset['price']
m1=pd.DataFrame(dataset['dist'].head())
m2=pd.DataFrame(x.head())
print("dist=")
print(np.matrix(m1))
print("price=")
print(np.matrix(m2))
from scipy.spatial import distance_matrix
dist_mat = distance_matrix(m1, m2, p=2)
print("distance matrix using Euclidian distance=")
print(dist_mat)
dist_mat1 = distance_matrix(m1, m2, p=1)
print("distance matrix using Manhatten distance=")
print(dist_mat1)
