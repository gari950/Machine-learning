from google.colab import drive
drive.mount('/content/drive')
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import preprocessing
data = pd.read_csv('/content/drive/MyDrive/Data Set/flats_moscow.csv') 
data.head()
data.describe()
normalized_data  =  (data  -  np.min(data))/(np.max(data)  -  np.min(data)) 
normalized_data.head()
normalized_data.describe()
data.plot(kind = "bar") 
plt.show()
normalized_data.plot(kind = "bar") 
plt.show()

