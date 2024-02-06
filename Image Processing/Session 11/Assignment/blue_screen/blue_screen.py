import cv2
import numpy as np

# Load the images
foreground_image = cv2.imread('SuperMan.jpg')
background_image = cv2.imread('pexels-aleksandar-pasaric-1619569.jpg')

# Resize background to match the foreground size
background_image = cv2.resize(
    background_image, (foreground_image.shape[1], foreground_image.shape[0]))

# Convert the images to HSV color space
hsv_foreground = cv2.cvtColor(foreground_image, cv2.COLOR_BGR2HSV)

# Define the range of green color in HSV
lower_green = np.array([37, 25, 25])
upper_green = np.array([75, 255, 255])

# Create a mask for detecting green color
mask = cv2.inRange(hsv_foreground, lower_green, upper_green)

# Invert the mask to get the non-green areas
mask_inv = cv2.bitwise_not(mask)

# Use the mask to extract the foreground object (Superman) from the green screen
foreground = cv2.bitwise_and(foreground_image, foreground_image, mask=mask_inv)

# Use the inverted mask to keep the background area from the background image
background = cv2.bitwise_and(background_image, background_image, mask=mask)

# Combine the foreground object with the new background
combined_image = cv2.add(foreground, background)

# Display the result
cv2.imwrite('blue_screen.jpg', combined_image)
cv2.imshow('Result', combined_image)
cv2.waitKey(0)
