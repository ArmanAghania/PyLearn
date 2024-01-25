def contour_area(contour):
    area = 0.0
    n = len(contour)

    for i in range(n):
        x1, y1 = contour[i][0]
        x2, y2 = contour[(i + 1) % n][
            0
        ]  # Ensures that the last point connects back to the first point
        area += x1 * y2 - x2 * y1

    return abs(area) / 2.0
