import cv2
import numpy as np

def create_mask(size, feather):
    mask = np.zeros(size, dtype=np.float32)
    cv2.rectangle(mask, (feather, feather), (size[1] - feather, size[0] - feather), (1, 1, 1), -1)
    cv2.blur(mask, (feather, feather), mask)
    return mask

feather_value = 20

image_1 = cv2.imread('brad.jpg')
image_2 = cv2.imread('scarlet.jpg')

height_1 = image_1.shape[0]
height_2 = image_2.shape[0]

diff = height_2 - height_1

image_2 = image_2[:-diff, :]

print(image_1.shape, image_2.shape)

image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

image_1_faces = face_detector.detectMultiScale(image_1, scaleFactor=1.3)
image_2_faces = face_detector.detectMultiScale(image_2, scaleFactor=1.3)


if len(image_1_faces) > 0 and len(image_2_faces) > 0:

    x1, y1, w1, h1 = image_1_faces[0]
    x2, y2, w2, h2 = image_2_faces[0]

    face_1 = image_1[y1:y1+h1, x1:x1+w1]
    face_2 = image_2[y2:y2+h2, x2:x2+w2]

    face_1 = cv2.resize(face_1, (w1, h1))
    face_2 = cv2.resize(face_2, (w1, h1))

    face_1 = face_1.astype(np.float32)
    face_2 = face_2.astype(np.float32)

    results = []

    for i in range(5):
        alpha = i / 4
        blended_face = cv2.addWeighted(face_1 * (1 - alpha), 1, face_2 * alpha, 1, 0)

        blended_face = blended_face.astype(np.uint8)

        mask = create_mask((h1, w1), feather_value)

        result = image_1.copy()

        y_slice = slice(y1, y1 + h1)
        x_slice = slice(x1, x1 + w1)

        result[y_slice, x_slice] = result[y_slice, x_slice] * (1 - mask) + blended_face * mask

        results.append(result)

    concatenated_result = cv2.hconcat(results)

    cv2.imwrite('morphed_faces_progression.jpg', concatenated_result)
    cv2.imshow('Morphed Faces Progression', concatenated_result)
    cv2.waitKey(0)
else:
    print("Faces not detected in one or both images")