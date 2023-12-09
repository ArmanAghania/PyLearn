import cv2

bat_image = cv2.imread('bat.jpg')
bat_image = cv2.cvtColor(bat_image, cv2.COLOR_BGR2GRAY)

_, bat_logo = cv2.threshold(bat_image, 100, 255, cv2.THRESH_BINARY)

cv2.imwrite('bat_logo.jpg', bat_logo)
cv2.imshow('result', bat_logo)
cv2.waitKey(0)