import time
import random
from progress.progress import Progress

def sleep():
  time.sleep(0.2)

spin = Progress("")
for i in range(20):
  print("Progress -> {0} <-".format(spin.next()), end="\r")
  sleep()
