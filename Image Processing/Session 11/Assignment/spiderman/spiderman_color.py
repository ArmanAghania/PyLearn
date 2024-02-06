import cv2
import numpy as np


def change_red_to_color(image, target_color):
    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define range of red color in HSV
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    # Threshold the HSV image to get only red colors
    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)

    # Convert the target color to HSV and prepare for assignment
    target_hsv_color = cv2.cvtColor(
        np.uint8([[target_color]]), cv2.COLOR_BGR2HSV)[0][0]

    # Correctly applying the target color to the red areas
    hsv_image[:, :, 0][red_mask > 0] = target_hsv_color[0]  # Hue
    hsv_image[:, :, 1][red_mask > 0] = target_hsv_color[1]  # Saturation

    # Convert back to BGR color space
    final_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    return final_image


# Load the image
image = cv2.imread('spiderman.jpg')

# Define the new color in BGR format (green and then yellow)
green_color = [0, 255, 0]
yellow_color = [0, 255, 255]

# Change red to green
green_spiderman = change_red_to_color(image, green_color)

# Change red to yellow
yellow_spiderman = change_red_to_color(image, yellow_color)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Green Spiderman', green_spiderman)
cv2.imshow('Yellow Spiderman', yellow_spiderman)
cv2.imwrite('green_spiderman.jpg', green_spiderman)
cv2.imwrite('yellow_spiderman.jpg', yellow_spiderman)
cv2.waitKey(0)
