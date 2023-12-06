import cv2
import numpy as np


while True:
    random_image = np.random.random((250, 350)) 
    cv2.imshow('result', random_image)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break