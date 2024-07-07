# EpochTasks

# Task_1

In Task 1 you have to run filter.py then plotter.py then kmeans.py

filter.py filters all the pincodes in Andhra Pradesh circle

plotter.py is when I observed that some data is corrupted and some swapped so I used the filtered_data.csv from filter.py then set some limits to the longitudes and latitudes that the Circle doesn't cross then if the data is not there it is removed and if it is there the data can be swapped if longitude is less than latitude then plotted them to give Figure_1 and outputs cleaned_data.csv

Kmeans.py takes cleaned_data.csv as input then using kmeans clustering formula with k=13(number of old districts in AP) and got Figure_2

And through that it was kind of obvious that the districts thoughh not nearly equal are still similar to the kmeans clutser map with centroid generally being closer to the districts HQ

Refrences-https://en.wikipedia.org/wiki/K-means_clustering