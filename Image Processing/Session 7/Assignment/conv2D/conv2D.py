import cv2
import numpy as np

# 1. Edge detection filter
kernel_1 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

# 2. Sharpening filter
kernel_2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

# 3. Emboss filter
kernel_3 = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])

# 4. Identity filter
kernel_4 = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

# 5. Gaussian blur filter
kernel_5 = np.array(
    [[1 / 16, 1 / 8, 1 / 16], [1 / 8, 1 / 4, 1 / 8], [1 / 16, 1 / 8, 1 / 16]]
)

image = cv2.imread("The-One-Piece-Movies-In-Order-1-1140x641.jpg", cv2.IMREAD_GRAYSCALE)

result_1 = cv2.filter2D(image, -1, kernel_1)
result_2 = cv2.filter2D(image, -1, kernel_2)
result_3 = cv2.filter2D(image, -1, kernel_3)
result_4 = cv2.filter2D(image, -1, kernel_4)
result_5 = cv2.filter2D(image, -1, kernel_5)

result = np.hstack((image, result_1, result_2, result_3, result_4, result_5))

cv2.imwrite("result.jpg", result)
cv2.imshow("image", result)
cv2.waitKey()
