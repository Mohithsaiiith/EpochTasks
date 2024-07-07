import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('alphabets_28x28.csv')

# Assuming the CSV has columns 'label' and 'pixels'
labels = data['label']
images = np.array([np.fromstring(pixel, dtype=int, sep=' ') for pixel in data['pixels']])

# Normalize the pixel values
images = images / 255.0

# Reshape images to 28x28
images = images.reshape(-1, 28, 28, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)
