# questa libreria di funzioni è realizzato a partire dai seguenti tutorial
# https://github.com/Uberi/speech_recognition/blob/master/README.rst
# https://www.programmareinpython.it/blog/riconoscimento-vocale-con-python-e-speechrecogniti/

import speech_recognition as sr
from PIL import Image, ImageTk

import cv2
import numpy as np

from threading import Thread

def ascolta():

    recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer

    with sr.Microphone() as source:
        #immagine(True)
        print("ti ascolto")
        recognizer_instance.adjust_for_ambient_noise(source)
        audio = recognizer_instance.listen(source)
        print("Ok! sto ora elaborando il messaggio!")
        #immagine(False)
    try:
        text = recognizer_instance.recognize_google(audio, language="it-IT")
        print("Google ha capito: \n", text)
        return text
    except Exception as e:
        print(e)
        return e


def immagine(colore):
    
    cv2.destroyWindow('Image')
    if(colore):
        img = cv2.imread('parla.jpg')
    else:
        img = cv2.imread('aspetta.jpg')

    cv2.imshow('image',img)
    cv2.waitKey(0)

