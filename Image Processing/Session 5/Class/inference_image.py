import numpy as np
import cv2
import tensorflow as tf
from functools import partial
import time
from OpenVtuber.TFLiteFaceDetector import UltraLightFaceDetecion
from OpenVtuber.TFLiteFaceAlignment import CoordinateAlignmentModel

fd = UltraLightFaceDetecion("OpenVtuber/weights/RFB-320.tflite",conf_threshold=0.88)
fa = CoordinateAlignmentModel("OpenVtuber/weights/coor_2d106.tflite")

# cap = cv2.VideoCapture(sys.argv[1])
image = cv2.imread('1.jpg')
color = (125, 255, 125)




start_time = time.perf_counter()

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    for i, p in enumerate(np.round(pred).astype(np.int64)):
        cv2.circle(image, tuple(p), 1, color, 1, cv2.LINE_AA)
        cv2.putText(image, str(i), tuple(p), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA )

    lips_landmarks = []
    for i in [52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]:
        lips_landmarks.append(pred[i])

    lips_landmarks = np.array(lips_landmarks, dtype=int)

x, y, w, h = cv2.boundingRect(lips_landmarks)
mask = np.zeros(image.shape, dtype=np.uint8)
cv2.drawContours(mask, [lips_landmarks], -1, (255, 255, 255), -1)

mask = mask // 255
result = image
# result = result[y:y+h, x:x+w]

# result_big = cv2.resize(result, (0, 0), fx=2, fy=2)
print(time.perf_counter() - start_time)

# cv2.imwrite('result.jpg', result)
cv2.imshow("result", result )
cv2.waitKey(0)