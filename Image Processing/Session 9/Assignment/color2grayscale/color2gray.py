import cv2
import numpy as np


def rgb2grayscale(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image cannot be loaded.")
        return None

    image = image.astype(float)

    B, G, R = image[:, :, 0], image[:, :, 1], image[:, :, 2]

    Grayscale = 0.299 * R + 0.587 * G + 0.114 * B

    Grayscale = Grayscale.astype(np.uint8)

    return Grayscale


image_path = 'The-One-Piece-Movies-In-Order-1-1140x641.jpg'
grayscale_image = rgb2grayscale(image_path)


cv2.imshow('Grayscale Image', grayscale_image)
cv2.waitKey(0)
cv2.imwrite('grayscale_luffy.jpg', grayscale_image)
