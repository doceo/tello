
from utlis import *

w,h = 360,240
pid = [0.5,0.5,0]
pError = 0
startCounter = 0  # for no Fligth = 1 per test senza takeoff

myDrone = intializeTello()

while True:
 
    ## flitght

    if startCounter == 0:
        myDrone.takeoff()
        startCounter = 1 

    ## STEP 1
    img = telloGetFrame(myDrone)
 
    ## STEP 2
    img, info = findFace(img)
 
    ## STEP 3  

    pError = trackFace(myDrone,info,w,pid,pError)

    print(info[0][0])

    # DISPLAY IMAGE
    cv2.imshow("MyResult", img)
 
    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) & 0xFF == ord('q'): # replace the 'and' with '&amp;' 
        myDrone.land()
        break


