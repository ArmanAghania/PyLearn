import cv2
import numpy as np
import os

images_path = os.listdir('data/galaxy')
print(images_path)

images = []
for image_path in images_path:
    image = cv2.imread('data/galaxy/' + image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    images.append(image)

result = np.zeros(image.shape)

for image in images:
    result = result + image

result = result / len(images)

result = result.astype(np.uint8)

cv2.imwrite('results/galaxy_result.jpg', result)
cv2.imshow('result', result)
cv2.waitKey(0)