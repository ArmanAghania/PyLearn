import cv2
import numpy as np

image = cv2.imread("lion.png", cv2.IMREAD_GRAYSCALE)

rows, cols = image.shape

kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

result = np.zeros((rows, cols), np.float32)

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        c = image[i - 1 : i + 2, j - 1 : j + 2]
        result[i, j] = np.abs(np.sum(kernel * c))

result = (result / np.max(result)) * 255
result = np.uint8(result)

cv2.imwrite("lion_edge.jpg", result)
