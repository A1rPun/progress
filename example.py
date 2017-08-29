import time
from progress.progress import Progress

def sleep():
  t = 0.01 * random.uniform(-0.1, 0.1)
  time.sleep(t)

spin = Progress()
for i in range(20):
  print(spin.next(), end="\r")
  sleep()
