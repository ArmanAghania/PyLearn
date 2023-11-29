import cv2

original_image = cv2.imread('itachi.jpg')
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

print(gray_image.shape)

start_point = (-10, 150)
end_point = (150, -10)

color = 0  
thickness = 30 

cv2.line(gray_image, start_point, end_point, color, thickness)

cv2.imwrite('dead_itachi.jpg', gray_image)
cv2.imshow('Dead Itachi', gray_image)
cv2.waitKey(0)
