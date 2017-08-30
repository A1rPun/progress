import time
from progress import Progress, Spin

PROGRESS = " -> {0} <- {1}s"
start = time.time()

for key in Spin.keys():
  spin = Progress(Spin[key])
  for i in range(20):
    t = round(time.time() - start)
    print(PROGRESS.format(spin.next(), t), end="\r")
    time.sleep(0.1)
  print(PROGRESS.format(spin.next(), t))

