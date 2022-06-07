Objective/ Aim:  to implement clustering on the given dataset using K-means clustering.

Data set URL: https://www.kaggle.com/datasets/shwetabh123/mall-customers

Tools: python

#Theory
A cluster refers to a collection of data points aggregated together because of certain similarities.
define a target number k, which refers to the number of centroids you need in the dataset. A centroid is the imaginary or real location representing the centre of the cluster.
Every data point is allocated to each of the clusters through reducing the in-cluster sum of squares.
In other words, the K-means algorithm identifies k number of centroids, and then allocates every data point to the nearest cluster, while keeping the centroids as small as possible.
The ‘means’ in the K-means refers to averaging of the data; that is, finding the centroid.

![image](https://user-images.githubusercontent.com/80147820/172343405-67d0b903-95ec-43e8-896d-7bd187385168.png)

 
#Implementation:-
1.	Select k points at random as centroids/cluster centers.
2.	Assign data points to the closest cluster based on Euclidean distance
3.	Calculate centroid of all points within the cluster
4.	Repeat iteratively till convergence. (Same points are assigned to the clusters in consecutive iterations)

#Advantages of using K means:-
1.	The algorithm in most cases runs in linear time.
2.	Simple and intuitive to understand
#Limitations of using K means:-
1.	A number of clusters need to be known beforehand.
2.	It is not very robust to outliers.
3.	Does not work very well with nonconvex shapes.
4.	Tries to generate equal-sized clusters

#output
![image](https://user-images.githubusercontent.com/80147820/172343523-7b6b33c6-8892-49ef-a0ed-4f41d57bc40b.png)

![image](https://user-images.githubusercontent.com/80147820/172343546-ec674c2b-f160-494a-a603-107214c7382c.png)
