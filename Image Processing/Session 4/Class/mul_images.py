import cv2
import numpy as np

image_1 = cv2.imread('data/c.tif')
mask = cv2.imread('data/d.tif')

image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY).astype(np.float32)
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY).astype(np.float32)

mask = mask / 255.0

result = cv2.multiply(image_1, mask)

cv2.imshow('result', result)
cv2.waitKey(0)