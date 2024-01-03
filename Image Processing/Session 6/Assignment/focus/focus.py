import cv2
import numpy as np


"""
Focusing on the object and bluring the background
"""

image = cv2.imread("flower_input.jpg", cv2.IMREAD_GRAYSCALE)


filter_size = 9
filter = np.ones((filter_size, filter_size), np.float32) / (filter_size**2)

x, y = image.shape

for i in range(filter_size // 2, x - filter_size // 2):
    for j in range(filter_size // 2, y - filter_size // 2):
        if 0 < image[i, j] < 50:
            sml = image[
                i - filter_size // 2 : i + filter_size // 2 + 1,
                j - filter_size // 2 : j + filter_size // 2 + 1,
            ]
            image[i, j] = np.sum(sml * filter)

cv2.imwrite("output_image.jpg", image)
