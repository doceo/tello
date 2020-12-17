import cv2 as cv
import numpy as np


## CODIFICA

import qrcode
from PIL import Image

img = qrcode.make('Your input text')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('https://medium.com/@ngwaifoong92')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

img.save("sample.png")



## DECODIFICA

# multiplo
im = cv.imread('sample.png')
det = cv.QRCodeDetector()
retval, decoded_info, points, straight_qrcode = det.detectAndDecodeMulti(np.hstack([im, im]))

# singolo
im = cv.imread('sample.png')
det = cv.QRCodeDetector()
retval, points, straight_qrcode = det.detectAndDecode(im)
