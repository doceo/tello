
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time


from utlis import *

w,h = 360,240

myDrone = intializeTello()

while True:
 
    ## STEP 1
    im = telloGetFrame(myDrone)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


    print(type(im))
    decodedObjects = decode(im)
    display(im, decodedObjects)

    # DISPLAY IMAGE
    cv2.imshow("MyResult", im)
 
    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) & 0xFF == ord('q'): # replace the 'and' with '&amp;' 
        myDrone.land()
        break