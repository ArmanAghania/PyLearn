import cv2
import numpy as np

image = cv2.imread('microsoft.jpg')
print(image.shape)

image_alpha = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

background_mask = np.all(image_alpha[:, :, :3] == [85, 85, 85], axis=-1)

image_alpha[background_mask, 3] = 0

cv2.imwrite('microsoft_transparent.png', image_alpha)
