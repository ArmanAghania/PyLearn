import cv2
import numpy as np

white_img = 255 * np.ones((400, 400), dtype=np.uint8)

height = 400

for px in range(height):
    
    gradient_value = int(255* (px/height))

    white_img[px, :] = gradient_value

cv2.imwrite("gradient_image.jpg", white_img)
cv2.imshow("White Image", white_img)
cv2.waitKey(0)
