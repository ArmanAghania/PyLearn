import cv2
import numpy as np

image = cv2.imread('The-One-Piece-Movies-In-Order-1-1140x641.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image

blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

inverted_blurred = 255 - blurred_image

sketch = cv2.divide(gray_image, inverted_blurred, scale=255 )

cv2.imwrite('sketch.png', sketch)
cv2.imshow('Sketch', sketch)
cv2.waitKey(0)