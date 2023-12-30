import cv2
import numpy as np
import time
from OpenVtuber.TFLiteFaceDetector import UltraLightFaceDetecion
from OpenVtuber.TFLiteFaceAlignment import CoordinateAlignmentModel

lip_indices = [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]
left_eye_indices = [89, 90, 87, 91, 93, 96, 94, 95]
right_eye_indices = [39, 42, 40, 41, 35, 36, 33, 37]

face_detector = UltraLightFaceDetecion("OpenVtuber\weights\RFB-320.tflite", conf_threshold=0.88)
face_aligner = CoordinateAlignmentModel("OpenVtuber\weights\coor_2d106.tflite")


def extract_feature(img, feature_indices):
    boxes, _ = face_detector.inference(img)
    for landmarks in face_aligner.get_landmarks(img, boxes):
        feature_points = np.array([landmarks[i] for i in feature_indices], dtype=int)
        rect = cv2.boundingRect(feature_points)
        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        cv2.drawContours(mask, [feature_points], -1, 255, -1)
        feature = cv2.bitwise_and(img, img, mask=mask)
        feature = feature[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
        # feature = cv2.rotate(feature, cv2.ROTATE_180)
        return feature, rect
    
def overlay_feature(img, feature_img, mask, rect):
    roi = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
    feature_img_masked = cv2.bitwise_and(feature_img, feature_img, mask=mask[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]])
    roi_masked = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(mask[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]))
    img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]] = cv2.add(roi_masked, feature_img_masked)

    
face_img = cv2.imread("face.jpg")

lip_mask, lip_rect = extract_feature(face_img, lip_indices)
lip_feature, _ = extract_feature(face_img, lip_indices)
lip_feature = cv2.rotate(lip_feature, cv2.ROTATE_180)
overlay_feature(face_img, lip_feature, lip_mask, lip_rect)

right_eye_mask, right_eye_rect = extract_feature(face_img, right_eye_indices)
right_eye_feature, _ = extract_feature(face_img, right_eye_indices)
right_eye_feature = cv2.rotate(right_eye_feature, cv2.ROTATE_180)
overlay_feature(face_img, right_eye_feature, right_eye_mask, right_eye_rect)

left_eye_mask, left_eye_rect = extract_feature(face_img, left_eye_indices)
left_eye_feature, _ = extract_feature(face_img, left_eye_indices)
left_eye_feature = cv2.rotate(left_eye_feature, cv2.ROTATE_180)
overlay_feature(face_img, left_eye_feature, left_eye_mask, left_eye_rect)

# Process the image
start_time = time.perf_counter()

face_img = cv2.rotate(face_img, cv2.ROTATE_180)

print("Processing Time:", time.perf_counter() - start_time)

cv2.imshow("face", face_img)
cv2.waitKey(0)

cv2.imwrite("scary_image.jpg", face_img)
