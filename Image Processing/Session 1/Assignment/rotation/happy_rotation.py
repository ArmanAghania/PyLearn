import cv2

img = cv2.imread('3.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   


face_1 = gray_img[0:1057, 0:960]
face_2 = gray_img[0:1057, 960:1920]

rotated_img = gray_img.copy()

rotated_face_1 = cv2.rotate(face_1, cv2.ROTATE_180)
rotated_face_2 = cv2.rotate(face_2, cv2.ROTATE_180)

rotated_img[0:1057, 0:960] = rotated_face_1
rotated_img[0:1057, 960:1920] = rotated_face_2


cv2.imwrite('happy.jpg', rotated_img)

cv2.imshow('image', rotated_img)

cv2.waitKey(0)