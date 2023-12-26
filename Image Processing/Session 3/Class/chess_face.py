import cv2

image = cv2.imread("860_main_beauty.png")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sticker = cv2.imread("102592-funny-emoji-boy-hd-image-free.png")
sticker_gray = cv2.cvtColor(sticker, cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = face_detector.detectMultiScale(image_gray, scaleFactor=1.3)
print(faces)

for face in faces:
    x, y, w, h = face
    face_image = image_gray[y : y + h, x : x + w]
    face_image_small = cv2.resize(face_image, [20, 20])

    face_image_big = cv2.resize(
        face_image_small, [w, h], interpolation=cv2.INTER_NEAREST
    )

    image_gray[y : y + h, x : x + w] = face_image_big

cv2.imwrite("chess_face.jpg", image_gray)
cv2.imshow("result", image_gray)
cv2.waitKey()
