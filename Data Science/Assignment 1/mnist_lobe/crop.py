from PIL import Image
import numpy as np

image_path = 'mnist.png'
original_image = Image.open(image_path)

image_array = np.array(original_image)

step_size = 20

cropped_images = []

for y in range(0, image_array.shape[0], step_size):
    for x in range(0, image_array.shape[1], step_size):
        # Define the bounding box for the current crop
        box = (x, y, x + step_size, y + step_size)
        # Crop the image and save it to the list
        cropped_image = original_image.crop(box)
        cropped_images.append(cropped_image)

cropped_image_paths = []
for i, img in enumerate(cropped_images):
    # Define the file path
    file_path = f'all_images/cropped_digit_{i}.png'
    # Save the image
    img.save(file_path)
    cropped_image_paths.append(file_path)