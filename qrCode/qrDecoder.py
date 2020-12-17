import cv2 as cv
import numpy as np


import qrcode
from PIL import Image

im = cv.imread('sample.png')
det = cv.QRCodeDetector()
retval, decoded_info, points, straight_qrcode = det.detectAndDecodeMulti(np.hstack([im, im]))

# singolo
im = cv.imread('sample.png')
det = cv.QRCodeDetector()
retval, points, straight_qrcode = det.detectAndDecode(im)
print (retval)

#  retval - Risultato in una stringa.
#  points- Matrice di vertici del quadrilatero del codice QR trovato. Sarà vuoto se non viene trovato.
#  straight_qrcode - Un'immagine contenente un codice QR rettificato e binarizzato.
