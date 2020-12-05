
from utlis import *

w,h = 360,240

myDrone = intializeTello()

while True:
 
    ## STEP 1
    img = telloGetFrame(myDrone)
 
    # DISPLAY IMAGE
    cv2.imshow("MyResult", img)
 
    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) & 0xFF == ord('q'): # replace the 'and' with '&amp;' 
        myDrone.land()
        break