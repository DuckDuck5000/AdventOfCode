class Read:

  def createArray():
    with open('testinput.txt', 'r') as file:
      lines = file.readlines()
      lines = [(line.rstrip()) for line in lines]
    nums = lines[0].split(',')
    return nums



class Solution:

  def __init__(self, data):
    self.nums = [int(line) for line in data]
    self.max = max(self.nums)
    self.min = min(self.nums)
  def costSolver(self, boolean):

    minCost = float('inf')

    for j in range(self.min, self.max+1):
      currFuel = 0

      for num in self.nums:
        distance = abs(j-num)
        if boolean:
          currFuel += distance
        else:
          currFuel += (distance*(distance+1)/2)
      
      minCost = min(minCost, currFuel)
    return int(minCost)

if __name__ == "__main__":

  data = Read().createArray()
  Answers = Solution(data)
  PartOne = Answers.costSolver(1)
  PartTwo = Answers.costSolver(0)

print(part1, part2)
