from djitellopy import Tello
import controller as ctr

tello  = Tello()

tello.connect()

tello.takeoff()

# 이동
tello.move_up(100)

go_val = 200

tello.move_left(int(go_val/2))
tello.move_forward(go_val)
tello.rotate_clockwise(92)
tello.move_forward(go_val*2)
tello.rotate_clockwise(92)
tello.move_forward(go_val*2)
tello.rotate_clockwise(92)
tello.move_forward(go_val*2)
tello.rotate_clockwise(93)
tello.move_forward(go_val)
tello.move_right(int(go_val/2))




try:
    tello.land()
except Exception as e:
    pass


pass