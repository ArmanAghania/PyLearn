import cv2
from mtcnn.mtcnn import MTCNN
import numpy as np
from PIL import Image
import math
import matplotlib.pyplot as plt

def EuclideanDistance(source_representation, test_representation):
    euclidean_distance = source_representation - test_representation
    euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance))
    euclidean_distance = np.sqrt(euclidean_distance)
    return euclidean_distance

def alignment_procedure(img, left_eye, right_eye):
    left_eye_x, left_eye_y = left_eye
    right_eye_x, right_eye_y = right_eye

    if left_eye_y > right_eye_y:
        point_3rd = (right_eye_x, left_eye_y)
        direction = -1
    else:
        point_3rd = (left_eye_x, right_eye_y)
        direction = 1

    a = EuclideanDistance(np.array(left_eye), np.array(point_3rd))
    b = EuclideanDistance(np.array(right_eye), np.array(point_3rd))
    c = EuclideanDistance(np.array(right_eye), np.array(left_eye))

    if b != 0 and c != 0:
        cos_a = (b*b + c*c - a*a)/(2*b*c)
        angle = np.arccos(cos_a)
        angle = (angle * 180) / math.pi

        if direction == -1:
            angle = 90 - angle

        img = Image.fromarray(img)
        img = np.array(img.rotate(direction * angle))

    return img

face_detector = MTCNN()

image_path = "oberyn-martell.jpg"
img = plt.imread(image_path)

results = face_detector.detect_faces(img)
if results:
    detection = results[0]
    x, y, width, height = detection['box']
    keypoints = detection["keypoints"]
    left_eye = keypoints["left_eye"]
    right_eye = keypoints["right_eye"]

    cropped_face = img[y:y+height, x:x+width]

    aligned_face = alignment_procedure(cropped_face.copy(), left_eye, right_eye)

    if aligned_face.shape[:2] != cropped_face.shape[:2]:
        aligned_face = cv2.resize(aligned_face, (cropped_face.shape[1], cropped_face.shape[0]))

    combined_face = np.hstack((cropped_face, aligned_face))

    plt.imshow(combined_face)
    plt.show()
    plt.imsave('combined_aligned.jpg', combined_face)

else:
    print("No faces detected.")

cv2.destroyAllWindows()
