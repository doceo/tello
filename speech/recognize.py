import speech_recognition as sr
from PIL import Image, ImageTk

import cv2
import numpy as np


from threading import Thread
import time



def immagine(colore):
    
    cv2.destroyWindow('Image')
    if(colore):
        img = cv2.imread('parla.jpg')
    else:
        img = cv2.imread('aspetta.jpg')

    cv2.imshow('image',img)
    cv2.waitKey(0)




class recognize (Thread):
    def __init__(self, nome, duration):
      Thread.__init__(self)
      self.nome = nome
      self.durata = duration
    def run(self):
        print ("Thread '" + self.name + "' avviato")

        recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer

        with sr.Microphone() as source:
            immagine(True)
            recognizer_instance.adjust_for_ambient_noise(source)
            audio = recognizer_instance.listen(source)
            print("Ok! sto ora elaborando il messaggio!")
            immagine(False)
        try:
            text = recognizer_instance.recognize_google(audio, language="it-IT")
            print("Google ha capito: \n", text)
            return text
        except Exception as e:
            print(e)
            return e

