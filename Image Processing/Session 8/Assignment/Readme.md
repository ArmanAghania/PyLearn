# Image Processing - Assingment 8

All the processing and image creations are done with opencv-python.

`https://sajjadaemmi.gitbook.io/pylearn/4.image-processing/4.8.assignment`


## 1. Histogram to Image 📊➡️🌅
* Apply five 2D filters with different kernels on your custom image. 

    Write a function to reconstruct image from a given histogram!

### Input:
![!Luffy](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%208/Assignment/histogram2image/The-One-Piece-Movies-In-Order-1-1140x641.jpg)

### Output:

![!bin_size_20](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%208/Assignment/histogram2image/recon_bin20.png)

![!bin_size_10](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%208/Assignment/histogram2image/recon_bin10.png)



## 2. Dice Recognition
Write a notebook for count the number of dots - that's the number on the dice.

Hint: use the hierarchy to find children and parent contours.

![!Dice](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%208/Assignment/dice_recognition/13.png)

![!Dice](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%208/Assignment/dice_recognition/55.png)

![!Dice](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%208/Assignment/dice_recognition/3.png)

![!Dice](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%208/Assignment/dice_recognition/2.png)


## 3. Implement cv2.boundingRect() function from scratch.

`x, y, w, h = cv2.boundingRect(contour)`



## 4. Implement cv2.contourArea() function from scratch.

`area = cv2.contourArea(contours)`


## 5. Implement cv2.findContours() function from scratch.

`contours, _ = cv2.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)`


## 6. A funny webcam application 😂


