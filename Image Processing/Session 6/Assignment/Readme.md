# Image Processing - Assingment 6

All the processing and image creations are done with opencv-python.

`https://sajjadaemmi.gitbook.io/pylearn/4.image-processing/4.6.assignment`


## 1. Histogram 📊
    * A. Write a function to get an image as input argument then calculate histogram and return it. 
    * B. Call the function, then visualize the result with plt.plot(), plt.hist() and plt.bar().

![!histogram](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/histogram/Histograms.png)


## 2. Foreground focus, Blur background 🌷
    A blurred background draws the focus to what’s important. It also often plays a part in differentiating the professional portrait 😍 from the casual snapshot 😐.
    Focus on the flower and blur the background.

![!focused_flower](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/focus/flower_input.jpg)


## 3. Edge detection 
    Use Laplacian Operator to detect edges of image.

![!lion_edge](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/edge_detection/lion_edge.jpg)
![!spider_edge](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/edge_detection/spider_edge.jpg)


## 4. Vertical and horizontal edge detection
    Use A suitable kernel to detect vertical and horizontal edges of image.

![!vertical_edge](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/vh_edge_detection/vertical_edges.jpg)
![!horizontal_edge](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/vh_edge_detection/horizontal_edges.jpg)


## 5. Noise reduction 🩻
    Mean filtering is a simple and easy to implement method of smoothing images. It is often used to reduce noise in images. The mean filter is computed using a convolution. The idea of mean filtering is simply to replace each pixel value in an image with the mean (average) value of its neighbors, including itself. Often a 3×3 square kernel is used, although larger kernels (e.g. 5×5 squares) can be used for more severe smoothing.

    Apply a 3x3 average filter to reduce noise in images. What happens if a 5x5 or a 15x15 filter is used?

![xray_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/xray_3x3.jpg)
![xray_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/xray_5x5.jpg)
![xray_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/xray_15x15.jpg)


![image_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/image_3x3.jpg)
![image_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/image_5x5.jpg)
![image_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/image_15x15.jpg)


![board_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/board_3x3.jpg)
![board_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/board_5x5.jpg)
![board_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/board_15x15.jpg)


