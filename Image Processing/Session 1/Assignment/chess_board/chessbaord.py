import cv2
import numpy as np

black_img = np.ones((400, 400), dtype=np.uint8)
copy_black_img = black_img.copy()
for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            copy_black_img[i*50:(i+1)*50, j*50:(j+1)*50] = 255



cv2.imwrite("Chess.png", copy_black_img)
cv2.imshow("Chess", copy_black_img)

cv2.waitKey(0)