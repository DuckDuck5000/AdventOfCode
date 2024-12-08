
class Read:

  def createArray(self):
    
    with open('input.txt', 'r') as file:
      lines = file.readlines()
      lines = [(line.rstrip()) for line in lines]
    return lines

class Solution:


  def __init__(self, data):

    self.data = data
    self.boards = []
    self.nums = []
    self.rows = {}
    self.cols = {}
    self.visited = {}
    self.targetSum = 0
  
  def initializeProblem(self):

    self.nums = self.data[0].split(',')
    self.boards = []
    self.rows = {}
    self.cols = {}
    self.visited = {}

    i = 2
    k = 0
    while i <= len(self.data):

      board = []
      for j in range(i, i+5):
        board.append(self.data[j].split())
      self.boards.append(board)
      self.cols[k] = {}
      self.rows[k] = {}
      self.visited[k] = [[False for _ in range(0, len(self.boards[0]))] for _ in range(0, len(self.boards[0]))]
      for l in range(0, len(board)):
        self.cols[k][l] = 0
        self.rows[k][l] = 0
      k += 1
      i += 6
      self.targetSum = len(self.boards[0])

  def partOne(self):

    self.initializeProblem()

    for num in self.nums:

      for k in range(0, len(self.boards)):

        for i in range(0, len(self.boards[k])):
          for j in range(0, len(self.boards[k][i])):

            if self.boards[k][i][j] == num:
              self.rows[k][j] += 1
              self.cols[k][i] += 1
              self.visited[k][i][j] = True

            if self.cols[k][i] == self.targetSum:
              tempSum = 0
              ## find sum 
              tempSum = self.traverseMatrix(k, i, True)
              return tempSum * int(num)
              for x in range(0, len(self.boards[k])):
                for y in range(0, len(self.boards[k][x])):
                  if x != i and self.visited[k][x][y] == False:
                    tempSum += int(self.boards[k][x][y])
              return tempSum * int(num)
            if self.rows[k][j] == self.targetSum:
              tempSum = 0
              ## find sum 
              for x in range(0, len(self.boards[k])):
                for y in range(0, len(self.boards[k][x])):
                  if x != j and self.visited[k][x][y] == False:
                    tempSum += int(self.boards[k][x][y])
              return tempSum * int(num)

  def partTwo(self):

    self.initializeProblem()
    boardsWon = [False for _ in range(0, len(self.boards))]
    for num in self.nums:

      for k in range(0, len(self.boards)):

        for i in range(0, len(self.boards[k])):
          for j in range(0, len(self.boards[k][i])):

            if self.boards[k][i][j] == num:
              self.rows[k][j] += 1
              self.cols[k][i] += 1
              self.visited[k][i][j] = True

            if self.cols[k][i] == self.targetSum:
              boardsWon[k] = True
              if sum(boardsWon) == len(self.boards):
                tempSum = 0
                for x in range(0, len(self.boards[k])):
                  for y in range(0, len(self.boards[k][x])):
                    if self.visited[k][x][y] == False:
                      tempSum += int(self.boards[k][x][y])

                return tempSum * int(num)
              
            if self.rows[k][j] == self.targetSum:
              boardsWon[k] = True
              if sum(boardsWon) == len(self.boards):
                tempSum = 0
                for x in range(0, len(self.boards[k])):
                  for y in range(0, len(self.boards[k][x])):
                    if self.visited[k][x][y] == False:
                      tempSum += int(self.boards[k][x][y])
                return tempSum * int(num)

if __name__ == "__main__":

  data = Read().createArray()
  Answers = Solution(data)
  PartOne = Answers.partOne()
  PartTwo = Answers.partTwo()
  print(PartOne)
  print(PartTwo)


  














