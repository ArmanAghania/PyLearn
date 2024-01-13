import cv2
import matplotlib.pyplot as plt

image = cv2.imread("board_noisy.png", cv2.IMREAD_GRAYSCALE)

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.plot(histogram)
plt.show()
