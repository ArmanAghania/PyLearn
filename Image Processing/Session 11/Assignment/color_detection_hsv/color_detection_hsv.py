import cv2
import numpy as np
import datetime

# Define color ranges in HSV
color_ranges = {
    'Red': ([0, 100, 100], [10, 255, 255]),
    'Green': ([35, 100, 100], [75, 255, 255]),
    'Blue': ([100, 150, 150], [140, 255, 255]),
    'Yellow': ([25, 100, 100], [35, 255, 255]),
    'Cyan': ([85, 100, 100], [100, 255, 255]),
    'Magenta': ([140, 100, 100], [170, 255, 255]),
    'Orange': ([10, 100, 100], [25, 255, 255]),
    'Purple': ([140, 50, 50], [160, 255, 255]),
    'Pink': ([160, 100, 100], [170, 255, 255]),
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower, upper)
        contours, _ = cv2.findContours(
            mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, color_name, (cx - 20, cy - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        filename = "frame_{}.png".format(
            datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
        cv2.imwrite(filename, frame)
        print("Saved:", filename)
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
