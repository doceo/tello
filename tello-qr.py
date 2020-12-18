
from utlis import *

w,h = 360,240

myDrone = intializeTello()

while True:
 
    ## STEP 1
    img = telloGetFrame(myDrone)
    
    pil = Image.open(stream)

    # inizializza lo scan dell'immagine
    scanner = zbar.ImageScanner()

    # configura il lettore
    scanner.parse_config('enable')

    pil = pil.convert('L')
    width, height = pil.size
    raw = pil.tostring()

    # wrap dati della immagine
    image = zbar.Image(width, height, 'Y800', raw)

    # cerca un QRcode
    scanner.scan(image)

    # DISPLAY IMAGE
    cv2.imshow("MyResult", img)
 
    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) & 0xFF == ord('q'): # replace the 'and' with '&amp;' 
        myDrone.land()
        break