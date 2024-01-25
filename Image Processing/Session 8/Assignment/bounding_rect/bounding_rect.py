def boundeing_rect(contour):
    min_x, min_y = contour[0][0]
    max_x, max_y = contour[0][0]

    for point in contour:
        x, y = point[0]

        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x

        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    width = max_x - min_x
    height = max_y - min_y

    return (min_x, min_y, width, height)
