import cv2
import numpy as np

room_image = cv2.imread('room_background.jpg')

new_floor = cv2.imread('room_foreground.jpg')

new_floor = cv2.resize(new_floor, (room_image.shape[1], room_image.shape[0]))

mask = cv2.imread('room_mask.jpg', 0)  

mask_expanded = np.repeat(mask[:, :, np.newaxis], 3, axis=2)


floor_replaced = np.where(mask_expanded == 255, new_floor, room_image)

cv2.imwrite('room_with_new_floor.jpg', floor_replaced)
cv2.imshow('Room with New Floor', floor_replaced)
cv2.waitKey(0)

