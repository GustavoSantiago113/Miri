import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

def wiener_deconvolution(blurred_image, kernel, noise_var):
    H = np.fft.fft2(kernel, s=blurred_image.shape)
    F = np.fft.fft2(blurred_image)
    G = (np.conj(H) / (np.abs(H) ** 2 + noise_var)) * F
    recovered_image = np.fft.ifft2(G).real
    return recovered_image

# Load your blurred image and kernel
blurred_image = plt.imread('blurred_image.jpg')
kernel = np.array([[1, 4, 6, 4, 1],
                   [4, 16, 24, 16, 4],
                   [6, 24, 36, 24, 6],
                   [4, 16, 24, 16, 4],
                   [1, 4, 6, 4, 1]]) / 256.0  # Example kernel

# Add simulated noise to the blurred image
noise_var = 0.01
noisy_blurred_image = blurred_image + np.random.normal(0, np.sqrt(noise_var), blurred_image.shape)

# Perform Wiener deconvolution
recovered_image = wiener_deconvolution(noisy_blurred_image, kernel, noise_var)

# Display the images
plt.subplot(131), plt.imshow(blurred_image, cmap='gray'), plt.title('Blurred Image')
plt.subplot(132), plt.imshow(noisy_blurred_image, cmap='gray'), plt.title('Noisy Blurred Image')
plt.subplot(133), plt.imshow(recovered_image, cmap='gray'), plt.title('Recovered Image')
plt.show()