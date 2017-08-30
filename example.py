import time
from progress import Progress, Spin

PROGRESS = "Progress -> {0} <-"

for key in Spin.keys():
  spin = Progress(Spin[key])
  for i in range(20):
    print(PROGRESS.format(spin.next()), end="\r")
    time.sleep(0.1)
  print(PROGRESS.format(spin.next()))
