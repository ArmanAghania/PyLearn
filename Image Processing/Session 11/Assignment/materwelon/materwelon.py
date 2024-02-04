import cv2
import numpy as np


def convert_to_materwelon(image_path):
    """
    Converts the red and green colors of an image to make reds look like greens and vice versa.
    This is intended to simulate a watermelon color swap effect on the image.

    :param image_path: Path to the input image.
    :return: The color swapped image as a numpy array in BGR format.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(
            "Image cannot be loaded from the provided path.")

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red1, upper_red1 = np.array([0, 50, 50]), np.array([10, 255, 255])
    lower_red2, upper_red2 = np.array([160, 50, 50]), np.array([180, 255, 255])
    lower_green, upper_green = np.array([35, 50, 50]), np.array([85, 255, 255])

    mask_red = cv2.inRange(hsv_image, lower_red1, upper_red1) + \
        cv2.inRange(hsv_image, lower_red2, upper_red2)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)

    RED_TO_GREEN_HUE_ADJUST = 55
    GREEN_TO_RED_HUE_ADJUST = 120
    hsv_image[:, :, 0] = np.where(
        mask_red > 0, (hsv_image[:, :, 0] + RED_TO_GREEN_HUE_ADJUST) % 180, hsv_image[:, :, 0])
    hsv_image[:, :, 0] = np.where(
        mask_green > 0, (hsv_image[:, :, 0] + GREEN_TO_RED_HUE_ADJUST) % 180, hsv_image[:, :, 0])

    return cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)


image_path = 'watermelon.jpg'
image = convert_to_materwelon(image_path)
cv2.imshow('Watermelon Color Swapped', image)
cv2.waitKey(0)
