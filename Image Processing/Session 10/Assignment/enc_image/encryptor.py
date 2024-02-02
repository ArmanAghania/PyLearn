from PIL import Image
import numpy as np
import os


def encrypt_image(image_path):
    # Load the image
    img = Image.open(image_path)
    img_arr = np.array(img)

    # Generate a random secret key with the same shape as the image array
    secret_key = np.random.randint(0, 256, size=img_arr.shape, dtype=np.uint8)

    # Encrypt the image using XOR operation
    encrypted_img_arr = np.bitwise_xor(img_arr, secret_key)

    # Save the encrypted image and the secret key
    encrypted_img = Image.fromarray(encrypted_img_arr)
    encrypted_img.save('encrypted_image.bmp')
    np.save('secret_key.npy', secret_key)


if __name__ == "__main__":
    image_path = 'path_to_image.jpg'
    encrypt_image(image_path)
