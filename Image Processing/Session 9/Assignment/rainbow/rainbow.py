import numpy as np
import cv2


def draw_rainbow():
    height, width = 800, 1200
    image = np.ones((height, width, 3), np.uint8) * 255

    colors = [
        (255, 0, 0),      # Red
        (255, 127, 0),    # Orange
        (255, 255, 0),    # Yellow
        (0, 255, 0),      # Green
        (0, 0, 255),      # Blue
        (75, 0, 130),     # Indigo
        (148, 0, 211)     # Violet
    ]

    center_x, center_y = width // 2, height

    radius = 300
    thickness = 50

    for color in reversed(colors):
        start_angle = 180
        end_angle = 360
        cv2.ellipse(image, (center_x, center_y), (radius, radius),
                    0, start_angle, end_angle, color, thickness)
        radius += thickness - 2
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return image


image = draw_rainbow()

cv2.imshow('Rainbow', image)
cv2.waitKey(0)
cv2.imwrite('rainbow.jpg', image)
