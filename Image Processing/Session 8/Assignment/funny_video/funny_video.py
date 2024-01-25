import cv2
import numpy as np

# Initialize video captures
video_file_capture = cv2.VideoCapture("funny_webcam_application.mp4")
webcam_capture = cv2.VideoCapture(0)

# Get dimensions of the webcam feed
ret, webcam_frame = webcam_capture.read()
webcam_height, webcam_width = webcam_frame.shape[:2]
print(webcam_height, webcam_width)

# Get dimensions of the video feed
ret, video_frame = video_file_capture.read()
video_height, video_width = video_frame.shape[:2]
print(video_height, video_width)

# Define size for the output video
output_size = (video_width, video_height)

# Video writer setup
fps = 40
output_video = cv2.VideoWriter(
    "output/javad.mp4", cv2.VideoWriter_fourcc(*"XVID"), fps, output_size, False
)
is_paused = False

while True:
    if not is_paused:
        ret, video_frame = video_file_capture.read()

    ret, webcam_frame = webcam_capture.read()
    webcam_resized = cv2.resize(webcam_frame, (video_width + 200, video_height - 200))
    webcam_flipped = cv2.flip(webcam_resized, 1)

    gray_video_frame = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
    gray_webcam_frame = cv2.cvtColor(webcam_flipped, cv2.COLOR_BGR2GRAY)

    # Overlay webcam feed onto video feed
    gray_video_frame[274:424, 130:280] = gray_webcam_frame[274:424, 130:280]

    # Write and display the frame
    output_video.write(gray_video_frame)
    cv2.imshow("Video Output", gray_video_frame)

    # Keyboard controls
    key = cv2.waitKey(25) & 0xFF
    if key == ord("s"):
        is_paused = True
    elif key == ord("p"):
        is_paused = False
    elif key == ord("q"):
        break

# Release resources
video_file_capture.release()
webcam_capture.release()
output_video.release()
cv2.destroyAllWindows()
