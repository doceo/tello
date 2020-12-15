# definisco la classe per gestire i thread

from threading import Thread
import time
class unThread (Thread):
   def __init__(self, nome, durata):
      Thread.__init__(self)
      self.nome = nome
      self.durata = durata
   def run(self):
      print ("Thread '" + self.name + "' avviato")
      time.sleep(self.durata)
      print ("Thread '" + self.name + "' terminato")

from random import randint
# Creazione dei thread
thread1 = unThread("Thread#1", randint(1,100))
thread2 = unThread("Thread#2", randint(1,100))
thread3 = unThread("Thread#3", randint(1,100))
# Avvio dei thread
thread1.start()
thread2.start()
thread3.start()
# Join
thread1.join()
thread2.join()
thread3.join()
# Fine dello script
print("Fine")