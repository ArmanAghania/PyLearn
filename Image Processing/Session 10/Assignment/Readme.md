# Image Processing - Assingment 10
**Supplementary topics**

All the processing and image creations are done with opencv-python.

`https://sajjadaemmi.gitbook.io/pylearn/4.image-processing/4.10.assignment`


## 1. PNG (Portable Network Graphics)
Transparent your Microsoft logo and remove it's background.
Save result with .png format.

![!Microsoft](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/microsoft_transparent/microsoft_transparent.png)

## 2. Color Recognition
Write a program with webcam like Assignment 27 - 4 to recognize these colors:
Red - Green - Blue - Yellow - Orange - Purple - White - Black


![!Stuff](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/color_detection/frame_20240202_234241.png)

![!Stuff](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/color_detection/frame_20240202_234302.png)

![!Stuff](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/color_detection/frame_20240202_234338.png)

![!Stuff](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/color_detection/frame_20240202_234345.png)


## 3. MediaPipe
Use mediapipe to detect body landmarks on webcam stream.

![!Mediapipe](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/mediapipe/frame_20240203_022253.png)


## 4. PIL (Python Imaging Library) Don't use OpenCV 

* Read a color image with PIL.
* Write a متن فارسی on image.
* Calculate 3 histograms and show with plt.
* Equalizes the image histogram.
* Convert image to gray.
* Calculate histogram and show with plt.
* Equalizes the gray image histogram.

![!Channels](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/pil_edit/channels.png)

![!Gray_hist](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/pil_edit/gray_hist.png)

![!Equalized_hist](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/pil_edit/equal_hist.png)

![!Text_image](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/pil_edit/text.png)

## 5. Image Encryption and Decryption 🔐

**Image Encryption** is the process of converting a normal image into a cipher image using a secret key in such a way that unauthorized users can't access it.

**Image Decryption** is the process of converting the cipher image into the original image by employing the secret key. Mainly, decryption operation is like encryption operation but applies in reverse order.

* Write `encryptor.py` to get an image, then generate a random secret key and encrypt the image using secret key. Finally save the encrypted image as a `.bmp` file and save the secret key as a `.npy` file.

* Write `decryptor.py` to get a cipher image and a secret key, then convert the cipher image into the original image. Finally save the decrypted image as a `.jpg` file.

* Write `main.py` using PySide6 (Qt for Python) to show input and output in GUI.

### Input

![!Luffy](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/enc_image/The-One-Piece-Movies-In-Order-1-1140x641.jpg)



![!encrypted_luffy](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/enc_image/encrypted_image.bmp)



![!decrypted_luffy](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%2010/Assignment/enc_image/decrypted_image.jpg)