from easytello import tello
from functions import *


my_drone = tello.Tello()


while True:
    istruzione = ascolta()

    if (istruzione == 'vola'):
        my_drone.takeoff()

    #   for i in range(4):
    #	my_drone.forward(100)
    #	my_drone.cw(90)

    #   my_drone.flip("l")
    #   my_drone.flip("r")
    #   my_drone.land()

    if (istruzione == 'scendi') & 0xFF == ord('q'): 
        my_drone.land()
        cv2.destroyWindow('Image')
        break