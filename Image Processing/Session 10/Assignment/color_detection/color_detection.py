import cv2
import numpy as np
import datetime


color_ranges = {
    'Red': ([150, 0, 0], [255, 100, 100]),
    'Green': ([0, 100, 0], [0, 255, 0]),
    'Blue': ([0, 0, 150], [100, 100, 255]),
    'Yellow': ([150, 150, 0], [255, 255, 100]),
    'Orange': ([200, 100, 0], [255, 165, 0]),
    'Purple': ([100, 0, 150], [150, 50, 255]),
    'White': ([200, 200, 200], [255, 255, 255]),
    'Black': ([0, 0, 0], [50, 50, 50])
}

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Loop over the color ranges
    for color_name, (lower, upper) in color_ranges.items():
        # Create a mask for the color range
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower, upper)

        # Find contours in the mask
        contours, _ = cv2.findContours(
            mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Only proceed if at least one contour was found
        if contours:
            # Find the largest contour in the mask
            c = max(contours, key=cv2.contourArea)
            # Compute the center of the contour
            M = cv2.moments(c)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                # Draw the contour and center of the shape on the frame
                cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
                cv2.putText(frame, color_name, (cx - 20, cy - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        filename = "frame_{}.png".format(
            datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
        cv2.imwrite(filename, frame)
        print("Saved:", filename)

    # Break the loop
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
