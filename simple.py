from djitellopy import Tello
import controller as ctr

tello  = Tello()

tello.connect()

tello.takeoff()

ctr.TelloUI.openCmdWindow()

try:
    tello.land()
except Exception as e:
    pass


pass