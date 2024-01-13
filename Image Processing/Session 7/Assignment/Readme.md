# Image Processing - Assingment 7

All the processing and image creations are done with opencv-python.

`https://sajjadaemmi.gitbook.io/pylearn/4.image-processing/4.7.assignment`


## 1. Convolution 2D
* Apply five 2D filters with different kernels on your custom image. 

    ```# 1. Edge detection filter
        kernel = np.array([[-1 , -1 , -1],
                        [-1 ,  8 , -1],
                        [-1 , -1 , -1]])

        # 2. Sharpening filter
        kernel = np.array([[0  , -1 ,  0],
                        [-1 ,  5 , -1],
                        [0  , -1 ,  0]])

        # 3. Emboss filter
        kernel = np.array([[-2 , -1 ,  0],
                        [-1 ,  1 ,  1],
                        [0  ,  1 ,  2]])

        # 4. Identity filter
        kernel = np.array([[0  ,  0 ,  0],
                        [0  ,  1 ,  0],
                        [0  ,  0 ,  0]])

        # 5. Your filter
        kernel = # what ever you want```

* Use np.hstack() to place the output image next to the input image.

![!luffy](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/conv2D/result.jpg)


## 2. The Magic 🪄🔮
Use the average filter to reveal hidden things.

### Input

![!dice](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/magic/1.tif)

### Output

![!revealed_dice](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/magic/result.jpg)

## 3. Median Filter
Use median filter to reduce noise in images. How do you feel? Is the average filter better or the median filter?

### Input

![!gray](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/input/5.png)

![!woman](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/input/Medianfilterp.png)

![!baloons](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/input/balloons_noisy.png)

![!board](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/input/board_noisy.png)

![!bulb](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/input/image_noisy.png)

![!xray](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/input/xray_noisy.png)

### Output

![!gray](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/output/5.png)

![!woman](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/output/Medianfilterp.png)

![!baloons](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/output/balloons_noisy.png)

![!board](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/output/board_noisy.png)

![!bulb](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/output/image_noisy.png)

![!xray](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/median_filter/output/xray_noisy.png)


## 4. Histogram Equalization
We will learn the concepts of histogram equalization and use it to improve the contrast of our images.

### Input

![!landscape](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/hist_equalization/Unequalized_Hawkes_Bay_NZ.jpg)

![!airport](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/hist_equalization/4.png)


### Output

![!landscape](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/hist_equalization/Equalized_1.png)

![!airport](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/hist_equalization/Equalized_2.png)


## 5. Adaptive Histogram Equalization

### Input

![scene](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/hist_equalization/tsukuba_l.png)

### Output

* With Normal Histogram Equalization

![scene](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/hist_equalization/Equalized_3.png)

* With Clahe Histogram Equalization

![scene](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%207/Assignment/hist_equalization/clahe_Equalized_3.png)


![image_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/image_3x3.jpg)
![image_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/image_5x5.jpg)
![image_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/image_15x15.jpg)


![board_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/board_3x3.jpg)
![board_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/board_5x5.jpg)
![board_noise_reduction](https://github.com/ArmanAghania/PyLearn/blob/main/Image%20Processing/Session%206/Assignment/noise_reduction/board_15x15.jpg)


