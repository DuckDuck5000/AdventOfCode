class Read:

  def createArray(self):

    with open('input.txt', 'r') as file:
      lines = file.readlines()
      lines = [(line.rstrip()) for line in lines]
    return lines

class Solution:

  def __init__(self, data):

    self.data = data
    self.parsedArr = []
    self.dic1 = {}
    self.dic2 = {}
    self.parseLines()


  def parseLines(self):
    self.parsedArr = []
    for line in self.data:
  
      start, end = line.split('->')
      x1, y1 = start.split(',')
      x2, y2 = end.split(',')
      x1 = int(x1.strip())
      y1 = int(y1.strip())
      x2 = int(x2.strip())
      y2 = int(y2.strip())
      dx = (x2-x1)
      dy = (y2-y1)

      self.parsedArr.append([dx, dy, x1, y1])

  def partOne(self):

    for line in self.parsedArr:
      dx, dy, x1, y1 = line[0], line[1], line[2], line[3]
      for i in range(0, 1+max(abs(dx), abs(dy))):
        x = x1 + (1 if dx > 0 else (-1 if dx < 0 else 0 ))*i
        y = y1 + (1 if dy > 0 else (-1 if dy < 0 else 0 ))*i

        if dx == 0 or dy == 0:
          if (x,y) not in self.dic1:
            self.dic1[(x,y)] = 0
          self.dic1[(x,y)] += 1
    count = 0
    for key, value in self.dic1.items():

      if value > 1:
        count += 1
    return count

  def partTwo(self):

    for line in self.parsedArr:

      dx, dy, x1, y1 = line[0], line[1], line[2], line[3]

      for i in range(0, 1+max(abs(dx), abs(dy))):
        x = x1 + (1 if dx > 0 else (-1 if dx < 0 else 0 ))*i
        y = y1 + (1 if dy > 0 else (-1 if dy < 0 else 0 ))*i

        if (x,y) not in self.dic2:
          self.dic2[(x,y)] = 0
        self.dic2[(x,y)] += 1
    count = 0
    for key, value in self.dic2.items():

      if value > 1:
        count += 1
    return count

if __name__ == "__main__":

  data = Read().createArray()
  Answers = Solution(data)
  PartOne = Answers.partOne()
  PartTwo = Answers.partTwo()
  print(PartOne)
  print(PartTwo)
