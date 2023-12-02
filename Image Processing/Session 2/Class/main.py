import cv2

img = cv2.imread('luffy-gear-5-laughing-one-piece-hd-wallpaper-uhdpaper.com-603@1@l.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   

rows, cols = img_gray.shape

thresh = 100

for r in range(rows):
    for c in range(cols):
        if img_gray[r, c] > thresh:
            img_gray[r, c] = 255
        else:
            img_gray[r, c] = 0

img_gray[img_gray > thresh] = 255
img_gray[img_gray <= thresh] = 0

cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY, img_gray)
cv2.imshow('luffy.jpg', img_gray)

cv2.waitKey(0)