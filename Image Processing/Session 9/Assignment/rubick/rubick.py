import cv2
import numpy as np


def transform_colors(image):
    """
    Transforms colors of an image based on the original RGB values. Specifically:
    - If both blue and green channels are above 128, the pixel is set to red.
    - If both blue and red channels are above 128, the pixel is set to green.
    - If both green and red channels are above 128, the pixel is set to blue.

    This operation ignores pixels where all three channels are above 128.

    Parameters:
    - image: np.ndarray, the input image in BGR format (as loaded by OpenCV).

    Returns:
    - np.ndarray, the image after applying the color transformations.
    """
    # Create masks based on color conditions
    mask_b_g = (image[:, :, 0] > 128) & (
        image[:, :, 1] > 128) & (image[:, :, 2] <= 128)
    mask_b_r = (image[:, :, 0] > 128) & (
        image[:, :, 2] > 128) & (image[:, :, 1] <= 128)
    mask_g_r = (image[:, :, 1] > 128) & (
        image[:, :, 2] > 128) & (image[:, :, 0] <= 128)

    # Apply transformations based on masks
    # For pixels where blue and green are dominant, change to red
    image[mask_b_g] = [0, 0, 255]  # BGR format for red

    # For pixels where blue and red are dominant, change to green
    image[mask_b_r] = [0, 255, 0]  # BGR format for green

    # For pixels where green and red are dominant, change to blue
    image[mask_g_r] = [255, 0, 0]  # BGR format for blue

    return image


def process_and_save_image(input_path, output_path):
    """
    Loads an image, transforms its colors based on specific rules, and saves the result.

    Parameters:
    - input_path: str, path to the input image.
    - output_path: str, path for saving the transformed image.
    """
    # Load the image
    image = cv2.imread(input_path)

    # Ensure the image was loaded successfully
    if image is None:
        print(f"Error: Failed to load the image from {input_path}")
        return

    # Transform the image colors
    transformed_image = transform_colors(image)

    # Save the transformed image
    cv2.imwrite(output_path, transformed_image)
    print(f"Image processed and saved to {output_path}")


if __name__ == "__main__":
    input_path = 'rubik.png'
    output_path = 'solved_cube.jpg'
    process_and_save_image(input_path, output_path)
