import cv2
import numpy as np

image = cv2.imread("board_noisy.png", cv2.IMREAD_GRAYSCALE)

# result = np.zeros(image.shape)

# for i in range(1, image.shape[0] - 1):
#     for j in range(1, image.shape[1] - 1):
#         small = image[i - 1 : i + 2, j - 1 : j + 2]
#         sorted = np.sort(small, axis=None)
#         result[i, j] = sorted[4]

result = cv2.medianBlur(image, 3)
cv2.imshow("image", result)
cv2.waitKey()
