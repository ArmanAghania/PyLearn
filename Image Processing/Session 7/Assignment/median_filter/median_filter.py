import cv2
import os

input_path = "input"

images = os.listdir(input_path)

print(images)

for image in images:
    if image == "balloons_noisy.png":
        img = cv2.imread(input_path + "/" + image)
        result = cv2.medianBlur(img, 5)
        cv2.imwrite("output/" + image, result)
        print("Converted " + image)
    else:
        img = cv2.imread(input_path + "/" + image)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        result = cv2.medianBlur(gray_img, 5)
        cv2.imwrite("output/" + image, result)
        print("Converted " + image)
