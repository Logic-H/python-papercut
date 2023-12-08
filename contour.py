import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Parameters for the size of the grid and number of levels
width, height = 200, 200
levels = 10

# Create a grid of points
x_idx = np.linspace(0, 1, width)
y_idx = np.linspace(0, 1, height)

# Generate random noise and then apply a Gaussian filter to create smooth transitions
data = np.random.rand(width, height)
data_smooth = gaussian_filter(data, sigma=20)

# Normalizing the data to make the contour levels evenly spaced
data_normalized = (data_smooth - np.min(data_smooth)) / (np.max(data_smooth) - np.min(data_smooth))

# Create contour plot with multiple levels
plt.figure(figsize=(8, 8))
contour = plt.contourf(x_idx, y_idx, data_normalized, levels=levels, cmap='Blues')
plt.axis('off')

# Invert the y-axis to match the coordinate system
plt.gca().invert_yaxis()

plt.show()
