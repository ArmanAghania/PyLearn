import cv2
import numpy as np

image_human = cv2.imread('data/human.jpg')
image_horse = cv2.imread('data/horse.jpg')


image_human = cv2.cvtColor(image_human, cv2.COLOR_BGR2GRAY)
image_horse = cv2.cvtColor(image_horse, cv2.COLOR_BGR2GRAY)

# result = image_human + image_horse
# result = cv2.add(image_human, image_horse)
# result = np.add(image_human, image_horse)
image_human = image_human.astype(np.float32)
image_horse = image_horse.astype(np.float32)

result = image_human + image_horse

result = result.astype(np.uint8)

cv2.imwrite('results/man_horse.jpg', result)

cv2.imshow('result', result)

cv2.waitKey(0)