from .spin import Spin

class Progress(object):
  def __init__(self, phases=""):
    self.index = 0
    self.phases = phases or Spin.phases[0]

  def next(self):
    s = self.phases[self.index]
    self.index = (self.index + 1) % len(self.phases)
    return s
