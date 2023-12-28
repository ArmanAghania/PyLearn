import cv2
import numpy as np

video_path = 'cars.mp4'
cap = cv2.VideoCapture(video_path)

sum_frames = None
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break  
    frame = frame.astype(np.float32)

    if sum_frames is None:
        sum_frames = np.zeros_like(frame)

    sum_frames += frame
    frame_count += 1

cap.release()

average_frame = (sum_frames / frame_count).astype(np.uint8)

cv2.imwrite('empty_road.jpg', average_frame)
cv2.imshow('Empty Road', average_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
