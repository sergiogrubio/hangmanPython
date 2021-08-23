# get current date/time
from datetime import datetime
# choose a random element from the list of words
from random import seed
from random import choice
import Stage

# now = datetime.now()

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)


class Game:
  def __init__(self, errors, words):
      self.timestamp = datetime.now()
      self.words = words
      self.errors = errors
      self.stage = Stage.Stage()

  def pickUpWord(self):
    # seed random number generator
    seed(datetime.now())
    # make a choice from the list of words
    self.word = choice(self.words)
    return(self.word)

  def start(self):
    self.stage.setWord(self.pickUpWord())
    self.stage.paint()
    #loop until no more chances
    while not self.stage.isCompleted():
      chr = input('Insert a single char:')
      if not self.stage.match(chr):
        self.errors = self.errors - 1
        if self.errors == 0:
          break
        print('Char "%s" not found. You can fail %i times more.' % (chr, self.errors))
      self.stage.paint()

  def end(self):
    if self.errors == 0:
      print("You lost!")
      print('The word was:', self.word)
    else:
      print("You won!")
    print("Elapsed time:", str(datetime.now() - self.timestamp))
