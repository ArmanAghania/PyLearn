import cv2
import numpy as np

black_image = np.zeros((250, 350), dtype=np.uint8)
white_image = np.ones((500, 800), dtype=np.uint8) * 255
random_image = np.random.random((250, 350))

cv2.rectangle(white_image, (30, 35), (350, 410), 128, 4)
cv2.circle(white_image, (600, 200), 100, 4)
cv2.line(white_image, (100,100), (700, 700), 90, 4)

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(white_image, 'PyLearn', (100, 150), font, 4, 90)
cv2.imshow("result", white_image)
cv2.waitKey(0)
