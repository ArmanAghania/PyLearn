import cv2
import numpy as np

image = np.zeros((500, 500), np.uint8)
points = np.array([[3, 40],
                  [14, 7],
                  [40, 40],
                  [50, 12]], dtype=int)

cv2.drawContours(image, [points], 0, (255, 255, 255), -1)
cv2.imshow("Image", image)
cv2.waitKey(0)