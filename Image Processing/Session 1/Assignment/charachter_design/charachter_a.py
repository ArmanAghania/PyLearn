import cv2
import numpy as np


black_img = np.ones((400, 400), dtype=np.uint8)
white_img = 255*black_img


block_size = 40
pattern_A = [
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1]
]

pattern_width = len(pattern_A[0]) * block_size
pattern_height = len(pattern_A) * block_size
start_x = (white_img.shape[1] - pattern_width) // 2
start_y = (white_img.shape[0] - pattern_height) // 2

for i, row in enumerate(pattern_A):
    for j, val in enumerate(row):
        if val == 1:
            top_left = (start_x + j * block_size, start_y + i * block_size)
            bottom_right = (start_x + (j + 1) * block_size, start_y + (i + 1) * block_size)
            cv2.rectangle(white_img, top_left, bottom_right, 0, -1)

cv2.imwrite('A.png', white_img)
cv2.imshow('A', white_img)
cv2.waitKey(0)

