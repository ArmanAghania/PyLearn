import cv2
import numpy as np

image_1 = cv2.imread('results/man_horse.jpg')
image_2 = cv2.imread('data/human.jpg')

image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)

# result = image_1 - image_2
# result = cv2.absdiff(image_1, image_2)
result = cv2.subtract(image_1, image_2)

cv2.imshow('result', result)
cv2.waitKey(0)