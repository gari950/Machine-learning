from google.colab import drive 
drive.mount('/content/drive') import pandas as pd
import numpy as np 
dataset= pd.read_csv('/content/drive/MyDrive/data set csp201/Iris_dup.csv') 
dataset.head()

# Size of dataset before handling redundancy
 print(“Size of dataset before handling redundancy:”)
 print(len(dataset.index))

# removing rows with redundant observations 
d=dataset.drop_duplicates()  
print(d.head())

# Size of dataset after handling redundancy 
print(“Size of dataset after handling redundancy:”) 
print(len(d.index))

# To find the correlation among
# the columns using pearson method 
correlations=dataset.corr(method ='pearson') 
import seaborn as sns
import matplotlib.pyplot as plt 
sns.heatmap(correlations) 
plt.show()
