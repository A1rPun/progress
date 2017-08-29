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
  def __init__(self, str):
    self.index = 0
    self.phases = str || loadings[0]
  
  def next(self):
    s = self.phases[self.index]
    self.index = (self.index + 1) % len(self.phases)
	return s
