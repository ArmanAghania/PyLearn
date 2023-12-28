import cv2
import numpy as np
import os

BASE_DIR = 'input'
image_folder_paths = os.listdir('input')
print(image_folder_paths)

images = {}
for i, image_folder_path in enumerate(image_folder_paths):
    images[i] = {}

    full_folder_path = os.path.join(BASE_DIR, image_folder_path)
    for j, image in enumerate(os.listdir(full_folder_path)):
        img_path = os.path.join(full_folder_path, image)
        img = cv2.imread(img_path)

        images[i][j] = img

for folder in images:
    for image_index in images[folder]:
        print(f"Folder {folder}, Image {image_index}: {images[folder][image_index].shape}")


averaged_images = {}

for folder in images:
    sum_image = None
    image_count = 0

    for image_index in images[folder]:
        img = images[folder][image_index]

        if img is not None:
            if sum_image is None:
                sum_image = np.zeros_like(img, np.float32)
            sum_image += img
            image_count += 1

    if image_count > 0:
        # Calculate the average
        avg_image = (sum_image / image_count).astype(np.uint8)
        averaged_images[folder] = avg_image
    else:
        print(f"No images found in folder {folder}")


if all(key in averaged_images for key in range(4)):
    top_row = np.hstack((averaged_images[0], averaged_images[1]))
    bottom_row = np.hstack((averaged_images[2], averaged_images[3]))
    whole_picture = np.vstack((top_row, bottom_row))

    # Save or display the whole picture
    cv2.imwrite('whole_picture.jpg', whole_picture)
    cv2.imshow('Whole Picture', whole_picture)
    cv2.waitKey(0)
else:
    print("Not all corner images are available to form the whole picture.")