from PIL import Image
import numpy as np


def decrypt_image(encrypted_image_path, secret_key_path):
    # Load the encrypted image and the secret key
    encrypted_img = Image.open(encrypted_image_path)
    encrypted_img_arr = np.array(encrypted_img)
    secret_key = np.load(secret_key_path)

    # Decrypt the image using XOR operation
    decrypted_img_arr = np.bitwise_xor(encrypted_img_arr, secret_key)

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_img_arr)
    decrypted_img.save('decrypted_image.jpg')


if __name__ == "__main__":
    decrypt_image('encrypted_image.bmp', 'secret_key.npy')
