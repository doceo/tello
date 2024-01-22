from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.move_right(100)
tello.rotate_clockwise(90)
tello.move_forward(50)
tello.rotate_clockwise(90)
tello.move_forward(50)
tello.rotate_clockwise(90)
tello.move_forward(50)
tello.rotate_clockwise(90)
tello.move_forward(50)

tello.land()

