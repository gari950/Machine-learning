Objective/ Aim: To analyse entity identification problem, redundancy and correlation analysis on a given sample dataset.

Data set URL: https: https://www.kaggle.com/code/sudiptog81/kpmg-virtual-internship-module-2/data

Tools: python

Theory:

What is Data Redundancy?
During data integration in data mining, various data stores are used. This can lead to the problem of redundancy in data. An attribute (column or feature of data set) 
is called redundant if it can be derived from any other attribute or set of attributes. Inconsistencies in attribute or dimension naming can also lead to the 
redundancies in data set.

![image](https://user-images.githubusercontent.com/80147820/172335849-687baf8c-5bad-48d6-8265-284e7189775d.png)



What is Correlation?
(to be exact Correlation in Statistic) is a measure of a mutual relationship between two variables whether they are causal or not. This degree of measurement
could be measured on any kind of data type (Continous and Continous, Categorical and Categorical, Continous and Categorical).
 
![image](https://user-images.githubusercontent.com/80147820/172335940-faded44d-4e30-40a6-b97d-318d1481b910.png)
 
output:

![image](https://user-images.githubusercontent.com/80147820/172342008-abc9bef6-2d16-4634-ac17-74734d40b473.png)

Size of dataset before handling redundancy:
150

# after removing rows with redundant observations

![image](https://user-images.githubusercontent.com/80147820/172342108-32f9b7cd-2b9b-440c-b4e7-0ebe5e09fa29.png)

Size of dataset after handling redundancy:
148

# Observation
Each square shows the correlation between the variables on each axis. Correlation ranges from -1 to
+1. Values closer to zero means there is no linear trend between the two variables. The close to 1 the correlation is the more positively correlated they are; that is as one increases so does the other and the closer to 1 the stronger this relationship is. A correlation closer to -1 is similar, but instead of both increasing one variable will decrease as the other increases. The diagonals are all 1 (white)because those squares are correlating each variable to itself (so it's a perfect correlation). For the rest the larger the number and darker the color the higher the correlation between the two variables. The plot is also symmetrical about the diagonal since the same two variables are being paired together in those squares.

![image](https://user-images.githubusercontent.com/80147820/172342232-14f5e3ef-773e-48eb-bf5c-fb805b7dac49.png)
