from djitellopy import Tello

# # 이동
# tello.move_up(100)

# go_val = 200

# tello.move_left(int(go_val/2))
# tello.move_forward(go_val)
# tello.rotate_clockwise(92)
# tello.move_forward(go_val*2)
# tello.rotate_clockwise(92)
# tello.move_forward(go_val*2)
# tello.rotate_clockwise(92)
# tello.move_forward(go_val*2)
# tello.rotate_clockwise(93)
# tello.move_forward(go_val)
# tello.move_right(int(go_val/2))




# try:
#     tello.land()
# except Exception as e:
#     pass


tello  = Tello()
tello.connect()

import cv2 as cv

panel = cv.imread('./mqdefault.jpg')
cv.imshow('tello control panel', panel)

move_val = 50

while True:
    key = cv.waitKey(1)
    if key == 27:
        break

    elif key == ord('t'):
        tello.takeoff()
    elif key == ord('l'):
        tello.land()
    
    
    # 업 다운
    elif key == ord('x'):
        tello.move('up',move_val)
    elif key == ord('z'):
        tello.move('down',move_val)
    #전후 좌우
    elif key == ord('w'):
        tello.move('forward',move_val)
    elif key == ord('a'):
        tello.move('left',move_val)
    elif key == ord('d'):
        tello.move('right',move_val)
    elif key == ord('s'):
        tello.move('back',move_val)
    
    # 좌/우 회전
    elif key == ord('e'):
        tello.rotate_clockwise(15)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(15)

pass