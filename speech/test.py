import cv2
import numpy as np

img = cv2.imread('parla.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX

cv2.imshow('image',img)

cv2.putText(img, "Parla ora!", (50, 100), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
cv2.imshow('image2',img)

cv2.waitKey(4000)
cv2.destroyWindow('Image')