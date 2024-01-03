import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
A function to get an image from user as input and visualize the histogram using plt.plot(), plt.hist(), plt.bar()
"""


def image_histogram(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    hist_values, bins, _ = plt.hist(
        image.ravel(), bins=256, range=[0, 256], color="gray"
    )
    plt.title("Histogram with plt.hist()")
    plt.xlabel("Intensity Value")
    plt.ylabel("Frequency")

    plt.subplot(1, 3, 2)
    plt.plot(bins[:-1], hist_values, color="black")
    plt.title("Histogram with plt.plot()")
    plt.xlabel("Intensity Value")
    plt.ylabel("Frequency")

    plt.subplot(1, 3, 3)
    plt.bar(bins[:-1], hist_values, width=1.0, color="gray")
    plt.title("Histogram with plt.bar()")
    plt.xlabel("Intensity Value")
    plt.ylabel("Frequency")

    plt.savefig("Histograms")
    plt.show()


image_path = input()
image_histogram(image_path)
