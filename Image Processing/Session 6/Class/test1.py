import numpy as np
import cv2

# Lowering Noise in Images

image = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
denoised_image = image.copy()
# denoised_image = cv2.fastNlMeansDenoising(image, None, 10, 7, 70)
rows, cols = image.shape
result = np.zeros((rows, cols), dtype=np.uint8)

# for i in range (10):
for i in range(1, rows-1):
    for j in range(1, cols-1):
        small = denoised_image[i-1:i+2, j-1:j+2]
        average = np.mean(small)
        result[i,j] = average
        # s = (denoised_image[i-1, j-1] + denoised_image[i-1, j] + denoised_image[i-1, j+1] + denoised_image[i, j-1] + denoised_image[i, j] + denoised_image[i, j+1] + denoised_image[i+1, j-1] + denoised_image[i+1, j] + denoised_image[i+1, j+1])/9
        # denoised_image[i, j] = s
        
combined_image = np.hstack((image, result))
cv2.imshow('Image', combined_image)
cv2.waitKey()