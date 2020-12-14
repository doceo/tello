
from utlis import *

w,h = 800,600

myDrone = intializeTello()

while True:
 
    ## STEP 1
    img = telloGetFrame(myDrone,w,h)
 
    ## STEP 2
    img, info = findFace(img)
    print(info[0][0])

    # DISPLAY IMAGE
    cv2.imshow("MyResult", img)
 
    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) & 0xFF == ord('q'): # replace the 'and' with '&amp;' 
        myDrone.land()
        break


