import cv2
import numpy as np

image_sajjad = cv2.imread('data/sajjad.jpg')
image_sajjad = cv2.cvtColor(image_sajjad, cv2.COLOR_BGR2GRAY)

image_lion = cv2.imread('data/lion.jpg')
image_lion = cv2.cvtColor(image_lion, cv2.COLOR_BGR2GRAY)

# result = image_sajjad + image_lion

# result = cv2.add(image_sajjad, image_lion)

# result = np.add(image_sajjad, image_lion)

image_sajjad = image_sajjad.astype(np.float32)
image_lion = image_lion.astype(np.float32)

# result = image_sajjad*2/3 + image_lion*1/3

result = image_sajjad*3/4 + image_lion*1/4


result = result.astype(np.uint8)

cv2.imshow('result', result)
cv2.waitKey(0)