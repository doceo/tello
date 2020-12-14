# questa libreria di funzioni è realizzato a partire dai seguenti tutorial
# https://github.com/Uberi/speech_recognition/blob/master/README.rst
# https://www.programmareinpython.it/blog/riconoscimento-vocale-con-python-e-speechrecogniti/

import speech_recognition as sr
from PIL import Image, ImageTk


def ascolta():

    recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer

    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source)
        print("Sono in ascolto... parla pure!")
        audio = recognizer_instance.listen(source)
        print("Ok! sto ora elaborando il messaggio!")
    try:
        text = recognizer_instance.recognize_google(audio, language="it-IT")
        print("Google ha capito: \n", text)
        return text
    except Exception as e:
        print(e)
        return e


#def parla():
    