import cv2
import numpy as np

kernel_1 = np.ones((5, 5), np.uint8) * 0.04
kernel_2 = np.ones((5, 5), np.uint8)
kernel_3 = np.ones((5, 5), np.uint8) * 5
kernel_4 = np.ones((3, 3), np.uint8) * 0.04
kernel_5 = np.ones((3, 3), np.uint8)
kernel_6 = np.ones((3, 3), np.uint8) * 5


image = cv2.imread("1.tif", cv2.IMREAD_GRAYSCALE)

result_1 = cv2.filter2D(image, -1, kernel_1)
result_2 = cv2.filter2D(image, -1, kernel_2)
result_3 = cv2.filter2D(image, -1, kernel_3)
result_4 = cv2.filter2D(image, -1, kernel_4)
result_5 = cv2.filter2D(image, -1, kernel_5)
result_6 = cv2.filter2D(image, -1, kernel_6)

result = np.hstack((result_1, result_2, result_3, result_4, result_5, result_6))

cv2.imwrite("result.jpg", result)
cv2.imshow("Original", result)
cv2.waitKey()
