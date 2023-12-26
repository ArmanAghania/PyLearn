import cv2
import numpy as np
import random

def resize_sticker_to_face_feature(sticker, feature_width, feature_height, scaling_factor=1.0):
    """Resize sticker to match the size of a face feature."""
    sticker_height, sticker_width = sticker.shape[:2]
    aspect_ratio = sticker_width / sticker_height
    new_width = int(feature_width * scaling_factor)
    new_height = int(new_width / aspect_ratio)
    resized_sticker = cv2.resize(sticker, (new_width, new_height))
    return resized_sticker

def overlay_sticker(frame, sticker, x, y, w, h):
    """Overlay a sticker on the frame with resizing and background removal."""
    sticker_resized = cv2.resize(sticker, (w, h))
    sticker_gray = cv2.cvtColor(sticker_resized, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(sticker_gray, 240, 255, cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask)

    roi = frame[y:y+h, x:x+w]
    fg = cv2.bitwise_and(sticker_resized, sticker_resized, mask=mask)
    bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    frame[y:y+h, x:x+w] = cv2.add(fg, bg)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
smile_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
sticker = cv2.imread("lion.png")
glasses_sticker = cv2.imread("sunglasses.png") 
lips_sticker = cv2.imread("lips.png") 
mode = 0

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for face in faces:
        x, y, w, h = face

        if mode == 1:
            sticker_resized_width = int(w * 1.2)
            sticker_resized_height = int(h * 1.2)
            sticker_x = x - (sticker_resized_width - w) // 2
            sticker_y = y - (sticker_resized_height - h) // 2

            resized_sticker = cv2.resize(sticker, (sticker_resized_width, sticker_resized_height))
            gray_sticker = cv2.cvtColor(resized_sticker, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(gray_sticker, 240, 255, cv2.THRESH_BINARY_INV)
            mask_inv = cv2.bitwise_not(mask)

            sticker_x = max(sticker_x, 0)
            sticker_y = max(sticker_y, 0)
            sticker_x_end = min(sticker_x + sticker_resized_width, frame.shape[1])
            sticker_y_end = min(sticker_y + sticker_resized_height, frame.shape[0])

            mask = cv2.resize(mask, (sticker_x_end - sticker_x, sticker_y_end - sticker_y))
            mask_inv = cv2.resize(mask_inv, (sticker_x_end - sticker_x, sticker_y_end - sticker_y))
            resized_sticker = cv2.resize(resized_sticker, (sticker_x_end - sticker_x, sticker_y_end - sticker_y))

            roi = frame[sticker_y:sticker_y_end, sticker_x:sticker_x_end]
            fg = cv2.bitwise_and(resized_sticker, resized_sticker, mask=mask)
            bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
            frame[sticker_y:sticker_y_end, sticker_x:sticker_x_end] = cv2.add(fg, bg)

        elif mode == 2:
            eyes = eye_detector.detectMultiScale(gray[y:y+h, x:x+w], scaleFactor=1.1, minNeighbors=5)
            smiles = smile_detector.detectMultiScale(gray[y:y+h, x:x+w], scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))

            if len(eyes) >= 2:
                sorted_eyes = sorted(eyes, key=lambda e: e[0])
                left_eye = sorted_eyes[0]
                right_eye = sorted_eyes[1]

                glasses_width = right_eye[0] + right_eye[2] - left_eye[0]
                glasses_height = max(left_eye[3], right_eye[3])
                glasses_x = x + left_eye[0]
                glasses_y = y + min(left_eye[1], right_eye[1])

                overlay_sticker(frame, glasses_sticker, glasses_x, glasses_y, glasses_width, glasses_height)

            if len(smiles) > 0:
                largest_smile = max(smiles, key=lambda s: s[2] * s[3])
                sx, sy, sw, sh = largest_smile
                lips_x, lips_y = x + sx, y + sy
                overlay_sticker(frame, lips_sticker, lips_x, lips_y, sw, sh)


        elif mode == 3:
            face_image = gray[y : y + h, x : x + w]
            face_image_small = cv2.resize(face_image, [20, 20])
            face_image_big = cv2.resize(face_image_small, [w, h], interpolation=cv2.INTER_NEAREST)

            face_image_big_bgr = cv2.cvtColor(face_image_big, cv2.COLOR_GRAY2BGR)
            frame[y : y + h, x : x + w] = face_image_big_bgr

        elif mode == 4:
            center_x = frame.shape[1] // 2

            left_side = frame[:, :center_x]
            right_side = frame[:, center_x:]

            mirrored_left_side = cv2.flip(left_side, 1)
            mirrored_right_side = cv2.flip(right_side, 1)

            combined_image = np.hstack((left_side, mirrored_left_side))

            frame = combined_image


    cv2.imshow('Webcam', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        mode = 1
    elif key == ord('2'):
        mode = 2
    elif key == ord('3'):
        mode = 3
    elif key == ord('4'):
        mode = 4
    elif key == ord('s'):
        filename = f"saved_frame{random.randint(0,100)}.jpg"  # Choose your path and filename
        cv2.imwrite(filename, frame)
        print(f"Frame saved as {filename}")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
