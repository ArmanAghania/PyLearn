import cv2
import numpy as np

image1 = cv2.imread('a.png') 
image2 = cv2.imread('b.png') 

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

result = cv2.absdiff(gray1, gray2)

_, result = cv2.threshold(result, 30, 255, cv2.THRESH_BINARY)  

cv2.imwrite('secret.png', result)
cv2.imshow('Secret Message', result)
cv2.waitKey(0)
