import cv2
import numpy as np


def detect_edges(image_path, save_path_v, save_path_h):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    rows, cols = image.shape

    kernel_v = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    kernel_h = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    result_v = np.zeros((rows, cols), np.float32)
    result_h = np.zeros((rows, cols), np.float32)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            c = image[i - 1 : i + 2, j - 1 : j + 2]
            result_v[i, j] = np.abs(np.sum(kernel_v * c))

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            c = image[i - 1 : i + 2, j - 1 : j + 2]
            result_h[i, j] = np.abs(np.sum(kernel_h * c))

    result_v = (result_v / np.max(result_v)) * 255
    result_v = np.uint8(result_v)

    result_h = (result_h / np.max(result_h)) * 255
    result_h = np.uint8(result_h)

    cv2.imwrite(save_path_v, result_v)
    cv2.imwrite(save_path_h, result_h)


image_path = "building.png"
detect_edges(image_path, "vertical_edges.jpg", "horizontal_edges.jpg")
