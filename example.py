import time
import random
from progress.progress import Progress

def sleep():
  t = 0.3
  time.sleep(t)

spin = Progress("")
for i in range(20):
  print(spin.next(), end="\r")
  sleep()
