import time
# import sys

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

class Progress
  def next():

def showLoading(str, t, to):
  str = str * t
  while(len(str)):
    s = str[:1]
    str = str[1:]
    print(s, end="\r")
    time.sleep(to)

times = 10 # int(sys.argv[1]) or 1
mode = 16 # int(sys.argv[2]) or 0
timeout = 0.1

showLoading(loadings[mode], times, timeout)
