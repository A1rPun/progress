loadings = [
  "|/-\\",
  "dqpb",
  "+x*",
  "⠟⠯⠷⠾⠽⠻",
  "⡿⣟⣯⣷⣾⣽⣻⢿",
  "◷◶◵◴",
  "◑◒◐◓",
  "⎺⎻⎼⎽⎼⎻",
  "◰◳◲◱",
  "▉▊▋▌▍▎▏▎▍▌▋▊▉",
  "←↖↑↗→↘↓↙",
  "┤┘┴└├┌┬┐",
  "◜◠◝◞◡◟",
  "☱☲☴",
  "▓▒░▒",
  "◢◣◤◥",
  "▁▃▄▅▆▇█▇▆▅▄▃",
  "⠁⠂⠄⡀⢀⠠⠐⠈",
  ".oO°Oo.",
  "🚶🏃",
  "🌍🌎🌏",
  "⬆️↗️➡️↘️⬇️↙️⬅️↖️",
  "🌑🌒🌓🌔🌕🌝🌖🌗🌘🌚",
  "🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚"
]

class Progress:
  def __init__(self, loadingIndex=0):
    self.index = 0
    self.phases = loadings[loadingIndex]

  def next(self):
    s = self.phases[self.index]
    self.index = (self.index + 1) % len(self.phases)
    return s
