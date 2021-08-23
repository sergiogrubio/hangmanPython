import Game
import re
from urllib.request import urlopen

# Number of errors to play the game
NUMERRORS = 7

# I get the words from this file
url = "http://data.pr4e.org/intro.txt"
file = urlopen(url)
words = []
word = ''

for line in file:
    decoded_line = line.decode("utf-8")
    for it in re.findall('[a-z]+', decoded_line, flags=re.IGNORECASE):
      word = it.strip().lower()
      # I get only words logger than 5 characters
      if len(word)>5:
        if words.count(word) == 0:
          words.append(word)
words.sort()

myGame = Game.Game(NUMERRORS, words)
myGame.start()
myGame.end()
