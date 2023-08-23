import numpy as np
import matplotlib.pyplot as plt

def adaptive_histogram(image, num_bins=256):
    hist, bins = np.histogram(image, bins=num_bins, range=(0, 255))
    plateau_threshold = 10  # You can adjust this threshold as needed

    for i in range(1, num_bins - 1):
        if abs(hist[i] - hist[i - 1]) <= plateau_threshold and abs(hist[i] - hist[i + 1]) <= plateau_threshold:
            bins[i] = (bins[i - 1] + bins[i + 1]) / 2

    return bins

# Load your image
image = plt.imread('input_image.jpg')

# Convert image to grayscale if needed
if len(image.shape) == 3:
    image = np.mean(image, axis=2)

# Get the adaptive histogram bins
adaptive_bins = adaptive_histogram(image)

# Plot the histogram
plt.hist(image.flatten(), bins=adaptive_bins, color='b', alpha=0.7)
plt.show()