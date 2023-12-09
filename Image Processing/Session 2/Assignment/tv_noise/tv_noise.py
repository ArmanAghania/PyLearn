import cv2
import numpy as np
import imageio

fourcc = cv2.VideoWriter_fourcc(*'avc1') 
writer = cv2.VideoWriter('tv_noise.mp4', fourcc, 20.0, (350, 250))

while True:
    random_image = np.random.random((250, 350, 3))  
    random_image = (random_image * 255).astype(np.uint8)  
    random_image = cv2.cvtColor(random_image, cv2.COLOR_BGR2GRAY)
    writer.write(random_image)  
    cv2.imshow('result', random_image)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

writer.release() 


reader = imageio.get_reader('tv_noise.mp4')
fps = reader.get_meta_data()['fps']
writer = imageio.get_writer('tv_noise.gif', fps=fps)

for frame in reader:
    writer.append_data(frame)

writer.close()

