from djitellopy import Tello

tello  = Tello()
tello.connect()

tello.streamon()

frame_read = tello.get_frame_read()
# 한장씩 읽어들인다.




import cv2 as cv

while True:
    cv.imshow('tello stream', frame_read.frame)
    key = cv.waitKey(1)
    if key == 27:
       break



tello.streamoff()

pass