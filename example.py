import time
import random
from progress import Progress, Spin

def sleep():
  time.sleep(0.1)

for j in range(len(Spin.phases)):
  spin = Progress(Spin.phases[j])
  for i in range(20):
    print("Progress -> {0} <-".format(spin.next()), end="\r")
    sleep()
  print("Progress -> {0} <-".format(spin.next()))
