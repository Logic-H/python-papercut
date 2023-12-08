import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from matplotlib import cm
from skimage import measure

# Simulating the SimplexNoise function
def generate_simplex_noise(m, n, seed, scale, amplitude):
    np.random.seed(seed)
    # Generate random noise
    noise = np.random.randn(m, n)
    # Apply gaussian filter to simulate Simplex noise
    noise = gaussian_filter(noise, sigma=scale) * amplitude
    return noise

# Function to generate and plot contours
# Revised function to generate and plot contours for each level
def generate_and_plot_contours(m, n, levels, noise):
    # Create a figure to plot the contours
    fig, axs = plt.subplots(len(levels), 1, figsize=(6, 3 * len(levels)))

    # Plot each level's contour on a subplot
    for i, level in enumerate(levels):
        ax = axs[i] if len(levels) > 1 else axs
        # Find contours at this level
        contours = measure.find_contours(noise, level=level)
        # Plot the image and the contour
        ax.imshow(noise, cmap=cm.gray)
        for contour in contours:
            ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
        ax.set_title(f'Contour at level: {level:.2f}')
        ax.axis('off')

    plt.tight_layout()
    plt.show()

# Now we call the revised function with the correct parameters



# Configurations similar to the provided JavaScript logic
config = {
    "randomScale": 3,
    "randomAmplitude": 1,
    "randomOffset": 0.5,
    "paperCount": 5
}

# Size of the grid
m, n = 200, 200

# Generating Simplex-like noise
noise = generate_simplex_noise(m, n, seed=0, scale=config["randomScale"], amplitude=config["randomAmplitude"])

# Normalizing the noise values
noise = (noise - noise.min()) / (noise.max() - noise.min())

# Creating threshold levels based on the number of paper cuts
levels = np.linspace(noise.min() + config["randomOffset"], noise.max(), config["paperCount"])

# Generate and plot the contours
generate_and_plot_contours(m, n, levels, noise)
