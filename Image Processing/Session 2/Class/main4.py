import cv2

cap = cv2.VideoCapture(0)

while True:
    _, image = cap.read()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('result', image)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break