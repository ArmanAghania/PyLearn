import cv2
import numpy as np


def apply_mean_filter(image_path, kernel_size):
    image = cv2.imread(image_path)

    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2)

    result = cv2.filter2D(image, -1, kernel)

    return result


image_path = "board_noisy.png"
result_3x3 = apply_mean_filter(image_path, 3)
result_5x5 = apply_mean_filter(image_path, 5)
result_15x15 = apply_mean_filter(image_path, 15)

cv2.imwrite("board_3x3.jpg", result_3x3)
cv2.imwrite("board_5x5.jpg", result_5x5)
cv2.imwrite("board_15x15.jpg", result_15x15)
