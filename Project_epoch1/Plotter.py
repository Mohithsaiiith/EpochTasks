import pandas as pd
import matplotlib.pyplot as plt


file_path = 'filtered_data.csv'
data = pd.read_csv(file_path)

circle_name = 'Andhra Pradesh Circle'

data = data.dropna(subset=['Latitude', 'Longitude'])


latitude_range = (12.5, 19.5)
longitude_range = (76.5, 84.5)


def correct_lat_long(row):
    lat, lon = row['Latitude'], row['Longitude']
    if not (latitude_range[0] <= lat <= latitude_range[1]) and (longitude_range[0] <= lon <= longitude_range[1]):
        
        row['Latitude'], row['Longitude'] = lon, lat
    return row


data = data.apply(correct_lat_long, axis=1)


data = data[(data['Latitude'] >= latitude_range[0]) & (data['Latitude'] <= latitude_range[1]) & 
            (data['Longitude'] >= longitude_range[0]) & (data['Longitude'] <= longitude_range[1])]

cleaned_data = data


cleaned_data.to_csv('cleaned_data.csv', index=False)


latitude = data['Latitude'].values
longitude = data['Longitude'].values


min_latitude = latitude.min()
max_latitude = latitude.max()
min_longitude = longitude.min()
max_longitude = longitude.max()

print(min_latitude, max_latitude, min_longitude, max_longitude)


plt.figure(figsize=(10, 6))
plt.scatter(longitude, latitude, c='blue', s=1 , marker='o')
plt.title(f'Geographical Distribution of Pincodes in {circle_name}')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.xlim(min_longitude, max_longitude)
plt.ylim(min_latitude, max_latitude)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
