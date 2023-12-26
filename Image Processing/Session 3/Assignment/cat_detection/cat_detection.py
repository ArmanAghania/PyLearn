import cv2
import random

image = cv2.imread("cats.jpeg")
# image = cv2.resize(image, (0, 0), fx=0.3, fy=0.3)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# sticker = cv2.imread("Problem-Too-Many-Cats-2048x1152.png")
# sticker_gray = cv2.cvtColor(sticker, cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalcatface.xml"
)

faces = face_detector.detectMultiScale(image_gray, scaleFactor=1.1)
cat_count = len(faces)

for face in faces:
    x, y, w, h = face
    cv2.rectangle(image_gray, [x, y], [x + w, y + h], 0, 2)


cv2.imwrite(f"{random.randint(1, 10)}.jpg", image_gray)
cv2.imshow("result", image_gray)
cv2.waitKey()
