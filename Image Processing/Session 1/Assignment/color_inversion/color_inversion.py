import cv2

def color_inversion(image):
    return abs(255 - image)

girl = cv2.imread('1.jpg')
boy = cv2.imread('2.jpg')


print(girl)
cv2.imshow('girl', color_inversion(girl))
cv2.imwrite('girl.jpg', color_inversion(girl))
cv2.imshow('boy', color_inversion(boy))
cv2.imwrite('boy.jpg', color_inversion(boy))

cv2.waitKey(0)