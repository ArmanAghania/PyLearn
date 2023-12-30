import numpy as np
import cv2
import time
from OpenVtuber.TFLiteFaceDetector import UltraLightFaceDetecion
from OpenVtuber.TFLiteFaceAlignment import CoordinateAlignmentModel

lip_indices = [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]
left_eye_indices = [89, 90, 87, 91, 93, 96, 94, 95]
right_eye_indices = [39, 42, 40, 41, 35, 36, 33, 37]

face_detector = UltraLightFaceDetecion("OpenVtuber\weights\RFB-320.tflite", conf_threshold=0.88)
face_aligner = CoordinateAlignmentModel("OpenVtuber\weights\coor_2d106.tflite")

face_img = cv2.imread("face.jpg")
fruit_img = cv2.imread('fruit.jpg')
fruit_img = cv2.resize(fruit_img, (200, 170))

def extract_feature(img, feature_indices):
    boxes, _ = face_detector.inference(img)
    for landmarks in face_aligner.get_landmarks(img, boxes):
        feature_points = np.array([landmarks[i] for i in feature_indices], dtype=int)
        rect = cv2.boundingRect(feature_points)
        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        cv2.drawContours(mask, [feature_points], -1, 255, -1)
        feature = cv2.bitwise_and(img, img, mask=mask)
        feature = feature[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
        feature = cv2.resize(feature, None, fx=4, fy=4, interpolation=cv2.INTER_LINEAR)
        return feature
    
lip_feature = extract_feature(face_img, lip_indices)
lip_feature = cv2.resize(lip_feature, (50, 20))

right_eye_feature = extract_feature(face_img, right_eye_indices)
right_eye_feature = cv2.resize(right_eye_feature, (40, 20))

left_eye_feature = extract_feature(face_img, left_eye_indices)
left_eye_feature = cv2.resize(left_eye_feature, (40, 20))

feature_mask = np.zeros((90, 90, 3), dtype=np.uint8)
feature_mask[0:20, 0:40] = right_eye_feature
feature_mask[0:20, 50:90] = left_eye_feature
feature_mask[30:50, 22:72] = lip_feature

x, y, w, h = 37, 70, 90, 90
for i in range(h):
    for j in range(w):
        if not np.any(feature_mask[i, j]):
            feature_mask[i, j] = fruit_img[y+i, x+j]

fruit_img[y:y+h, x:x+w] = feature_mask

cv2.imwrite('fruit_filter.png', fruit_img)
cv2.waitKey(0)
