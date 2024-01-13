import cv2
import matplotlib.pyplot as plt

# image_1 = cv2.imread("Unequalized_Hawkes_Bay_NZ.jpg", cv2.IMREAD_GRAYSCALE)
# image_2 = cv2.imread("4.png", cv2.IMREAD_GRAYSCALE)
image_3 = cv2.imread("tsukuba_l.png", cv2.IMREAD_GRAYSCALE)

# hist_1 = cv2.calcHist([image_1], [0], None, [256], [0, 256])
# hist_2 = cv2.calcHist([image_2], [0], None, [256], [0, 256])
hist_3 = cv2.calcHist([image_3], [0], None, [256], [0, 256])

# equalized_1 = cv2.equalizeHist(image_1)
# equalized_2 = cv2.equalizeHist(image_2)
equalized_3 = cv2.equalizeHist(image_3)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

crahlequalized_3 = clahe.apply(image_3)

# plt.plot(hist_3)
# plt.show()

# cv2.imwrite("Equalized_1.png", equalized_1)
# cv2.imwrite("Equalized_2.png", equalized_2)
cv2.imwrite("Equalized_3.png", equalized_3)
cv2.imwrite("clahe_Equalized_3.png", crahlequalized_3)


cv2.imshow("Equalized_3", crahlequalized_3)
cv2.waitKey()
