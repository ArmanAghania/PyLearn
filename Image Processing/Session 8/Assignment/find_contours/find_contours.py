import numpy as np
import cv2


def apply_sobel(image):
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)

    sobel_x = cv2.filter2D(image, -1, Gx)
    sobel_y = cv2.filter2D(image, -1, Gy)

    sobel = np.hypot(sobel_x, sobel_y)
    sobel = np.uint8(sobel / sobel.max() * 255)

    return sobel


def threshold_image(image, threshold=128):
    return (image > threshold).astype(np.uint8) * 255


def find_starting_point(binary_image):
    for y in range(binary_image.shape[0]):
        for x in range(binary_image.shape[1]):
            if binary_image[y, x] == 255:
                return x, y
    return None


def trace_contour(binary_image, start_point):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 4-connectivity
    backtrack = {0: 2, 1: 3, 2: 0, 3: 1}

    contour = []
    current_point = start_point
    current_dir = 0

    rows, cols = binary_image.shape

    while True:
        contour.append(current_point)
        binary_image[current_point[1], current_point[0]] = 0

        found_next = False
        for _ in range(4):
            next_point = (
                current_point[0] + directions[current_dir][0],
                current_point[1] + directions[current_dir][1],
            )

            # Check if next_point is within the image bounds
            if 0 <= next_point[0] < cols and 0 <= next_point[1] < rows:
                if binary_image[next_point[1], next_point[0]] == 255:
                    current_point = next_point
                    found_next = True
                    break

            current_dir = (current_dir + 1) % 4

        if not found_next:
            if len(contour) > 1:
                back_dir = backtrack[current_dir]
                back_point = (
                    current_point[0] + directions[back_dir][0],
                    current_point[1] + directions[back_dir][1],
                )

                # Check if back_point is within the image bounds
                if 0 <= back_point[0] < cols and 0 <= back_point[1] < rows:
                    if binary_image[back_point[1], back_point[0]] == 255:
                        current_point = back_point
                        current_dir = (back_dir + 2) % 4
                        continue

            break

    return contour


def find_contours(image):
    edged_image = apply_sobel(image)
    binary_image = threshold_image(edged_image)

    contours = []
    while True:
        start_point = find_starting_point(binary_image)
        if start_point is None:
            break
        contour = trace_contour(binary_image, start_point)
        if len(contour) > 5:  # Arbitrary threshold to ignore noise
            contours.append(contour)

    return contours


image = cv2.imread("unknown.png", cv2.IMREAD_GRAYSCALE)
contours = find_contours(image)
print(contours)
