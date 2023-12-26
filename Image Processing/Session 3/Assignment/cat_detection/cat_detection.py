import cv2
import random

image = cv2.imread("860_main_beauty.png")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sticker = cv2.imread("102592-funny-emoji-boy-hd-image-free.png")
sticker_gray = cv2.cvtColor(sticker, cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = face_detector.detectMultiScale(image_gray, scaleFactor=1.3)
cat_count = len(faces)

for face in faces:
    x, y, w, h = face
    cv2.rectangle(image_gray, [x, y], [x + w, y + h], 0, 2)


cv2.imwrite(f"{random.randint(1, 10)}.jpg", image_gray)
cv2.imshow("result", image_gray)
cv2.waitKey()
