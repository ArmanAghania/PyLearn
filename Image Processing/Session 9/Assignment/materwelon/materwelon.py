import cv2
import numpy as np


def convert_to_materwelon(image_path):
    image = cv2.imread(image_path)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if image is None:
        print("Error: Image cannot be loaded.")
        return

    red_channel = image[:, :, 2].copy()
    green_channel = image[:, :, 1].copy()

    image[:, :, 1] = red_channel
    image[:, :, 2] = green_channel

    return image


image_path = 'watermelon.jpg'
image = convert_to_materwelon(image_path)
cv2.imshow('Materwelon', image)
cv2.waitKey(0)

cv2.imwrite('materwelon.jpg', image)
