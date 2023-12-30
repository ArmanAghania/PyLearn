import numpy as np
import cv2
from OpenVtuber.TFLiteFaceDetector import UltraLightFaceDetecion
from OpenVtuber.TFLiteFaceAlignment import CoordinateAlignmentModel

def extract_and_enlarge_feature(img, feature_indices, scale_factor=2):
    boxes, _ = face_detector.inference(img)
    for landmarks in face_aligner.get_landmarks(img, boxes):
        feature_points = np.array([landmarks[i] for i in feature_indices], dtype=int)
        rect = cv2.boundingRect(feature_points)
        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        cv2.drawContours(mask, [feature_points], -1, 255, -1)
        feature = cv2.bitwise_and(img, img, mask=mask)
        feature = feature[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
        feature = cv2.resize(feature, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
        return feature, rect, scale_factor

def overlay_feature(original_img, feature_img, rect, scale_factor):
    x, y, w, h = rect
    center_x, center_y = x + w // 2, y + h // 2
    new_w, new_h = int(w * scale_factor), int(h * scale_factor)
    x_new, y_new = center_x - new_w // 2, center_y - new_h // 2

    resized_feature = cv2.resize(feature_img, (new_w, new_h))

    for i in range(new_h):
        for j in range(new_w):
            if np.all(resized_feature[i, j] < [50, 50, 50]): 
                if y_new + i < original_img.shape[0] and x_new + j < original_img.shape[1]:
                    resized_feature[i, j] = original_img[y_new + i, x_new + j]

    original_img[y_new:y_new + new_h, x_new:x_new + new_w] = resized_feature

    return original_img

face_detector = UltraLightFaceDetecion("OpenVtuber/weights/RFB-320.tflite", conf_threshold=0.88)
face_aligner = CoordinateAlignmentModel("OpenVtuber/weights/coor_2d106.tflite")

face_img = cv2.imread("face.jpg")

lip_indices = [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]
left_eye_indices = [89, 90, 87, 91, 93, 96, 94, 95]
right_eye_indices = [39, 42, 40, 41, 35, 36, 33, 37]

lip_feature, lip_rect, lip_scale = extract_and_enlarge_feature(face_img, lip_indices)
face_img = overlay_feature(face_img, lip_feature, lip_rect, lip_scale)

right_eye_feature, right_eye_rect, right_eye_scale = extract_and_enlarge_feature(face_img, right_eye_indices)
face_img = overlay_feature(face_img, right_eye_feature, right_eye_rect, right_eye_scale)

left_eye_feature, left_eye_rect, left_eye_scale = extract_and_enlarge_feature(face_img, left_eye_indices)
face_img = overlay_feature(face_img, left_eye_feature, left_eye_rect, left_eye_scale)

cv2.imwrite('enlarged_features.png', face_img)
cv2.waitKey(0)
