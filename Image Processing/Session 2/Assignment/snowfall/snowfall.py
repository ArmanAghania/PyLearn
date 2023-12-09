import cv2
import numpy as np
import imageio

def add_snowflakes(image, snowflakes):
    for (x, y, radius) in snowflakes:
        cv2.circle(image, (x, y), radius, 255, -1)
    return image

def update_snowflakes(snowflakes, image_shape):
    for i in range(len(snowflakes)):
        x, y, radius = snowflakes[i]
        y += np.random.randint(1, 4) 
        if y > image_shape[0]:
            y = 0  
        snowflakes[i] = (x, y, radius)
    return snowflakes

landscape = cv2.imread('winter_landscape.png')
landscape = cv2.resize(landscape, (600, 400))
landscape_bw = cv2.cvtColor(landscape, cv2.COLOR_BGR2GRAY)



num_snowflakes = 100
snowflakes = [(np.random.randint(0, landscape.shape[1]), 
               np.random.randint(0, landscape.shape[0]), 
               np.random.randint(1, 4)) for _ in range(num_snowflakes)]

fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video_writer = cv2.VideoWriter('snowfall.mp4', fourcc, 20.0, (landscape.shape[1], landscape.shape[0]), False)

for _ in range(200):
    frame = landscape_bw.copy()
    snowflakes = update_snowflakes(snowflakes, landscape.shape)
    frame_with_snowflakes = add_snowflakes(frame, snowflakes)
    video_writer.write(frame_with_snowflakes)
    # cv2.imshow('result', frame_with_snowflakes)

    # if cv2.waitKey(20) & 0xFF == ord('q'):
    #     break

video_writer.release()

reader = imageio.get_reader('snowfall.mp4')
fps = reader.get_meta_data()['fps']
writer = imageio.get_writer('snowfall.gif', fps=fps)

for frame in reader:
    writer.append_data(frame)

writer.close()
