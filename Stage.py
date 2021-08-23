class Stage:
  def __init__(self):
      self.list = []
      self.listStage = []

  def setWord(self, word):
    for item in word:
      self.list.append(item)
      self.listStage.append('-')

  def paint(self):
    print(self.listStage)

  def isCompleted(self):
    if self.listStage.count('-') != 0:
      return(False)
    else:
      return(True)
  
  def match(self, chr):
    found = False
    for i in range(0,len(self.list)):
      if self.list[i] == chr:
        self.listStage[i] = chr
        found = True
    return(found)
  

