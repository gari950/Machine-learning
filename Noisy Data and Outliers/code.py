#outlier
from google.colab import drive
import pandas as pd
drive.mount('/content/drive')
dataset= pd.read_csv('/content/drive/MyDrive/data set csp201/Placement_data_full_class.csv')
dataset.head()
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize = (10,10))
ax.set_xlabel('Salary')
x=dataset['salary']
ax.set_ylabel('hsc_p')
y=dataset['hsc_p']
plt.scatter(x,y)
plt.show()

# noisy data
import matplotlib.pyplot as plt
x=dataset['etest_p']
y=dataset['degree_p']
x1=sorted(x[0:])
y1=y[0:]
plt.plot(x1,y1,linestyle='-', linewidth=1,alpha=.5)
plt.plot(x1,y1,color='r')
plt.show()
 
