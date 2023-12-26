import cv2
import numpy as np


# Create a function to draw a football pitch
def draw_pitch():
    # Create a blank green "pitch" background
    pitch_length, pitch_width = 640, 1024
    stripe_width = pitch_width // 10  # 10 stripes for the pitch

    # Create a blank pitch with a base green color
    pitch = np.zeros((pitch_length, pitch_width, 3), np.uint8)

    # Use two shades of green for the stripes
    light_green = (0, 200, 0)
    dark_green = (0, 150, 0)

    # Draw alternating light and dark green stripes
    for i in range(10):
        start_x = i * stripe_width
        end_x = start_x + stripe_width
        color = light_green if i % 2 == 0 else dark_green
        cv2.rectangle(pitch, (start_x, 0), (end_x, pitch_length), color, -1)

    # Draw the outer boundary - 6 pixels for the line width
    cv2.rectangle(pitch, (10, 10), (1014, 630), (255, 255, 255), 6)

    # Draw the half-way line, centre circle and centre spot
    cv2.line(pitch, (512, 10), (512, 630), (255, 255, 255), 6)
    cv2.circle(pitch, (512, 320), 80, (255, 255, 255), 6)
    cv2.circle(pitch, (512, 320), 2, (255, 255, 255), 6)

    # Draw the left penalty area
    cv2.rectangle(pitch, (10, 160), (160, 480), (255, 255, 255), 6)
    cv2.rectangle(pitch, (10, 250), (70, 390), (255, 255, 255), 6)

    # Draw the right penalty area
    cv2.rectangle(pitch, (1014 - 150, 160), (1014, 480), (255, 255, 255), 6)
    cv2.rectangle(pitch, (1014 - 60, 250), (1014, 390), (255, 255, 255), 6)

    # Draw the penalty spots
    cv2.circle(pitch, (100, 320), 2, (255, 255, 255), 6)
    cv2.circle(pitch, (1014 - 90, 320), 2, (255, 255, 255), 6)

    # Draw the corner arcs
    cv2.ellipse(pitch, (10, 10), (20, 20), 0, 0, 90, (255, 255, 255), 6)
    cv2.ellipse(pitch, (10, 630), (20, 20), 0, 90, 180, (255, 255, 255), 6)
    cv2.ellipse(pitch, (1014, 10), (20, 20), 0, 270, 360, (255, 255, 255), 6)
    cv2.ellipse(pitch, (1014, 630), (20, 20), 0, 180, 270, (255, 255, 255), 6)

    return pitch


# Draw the pitch and save the image
soccer_pitch = draw_pitch()

cv2.imwrite("soccer_pitch.png", soccer_pitch)
cv2.imshow("pitch", soccer_pitch)
cv2.waitKey()
