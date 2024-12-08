class Read:

  def createArray(self):
    
    with open('input.txt', 'r') as file:
      lines = file.readlines()
      lines = [(line.rstrip()) for line in lines]
    return lines


class Solution:

  def __init__(self, data):

    self.input = data

  def partOne(self):

    ## initalize hashMap
    hashMap = {}

    for i in range(0, len(self.input[0])):
      hashMap[i] = [0, 0]

    for line in self.input:
      line = str(line)
      for i in range(0, len(line)):
        if int(line[i]) == 0:
          hashMap[i][0] += 1
        else:
          hashMap[i][1] += 1


    ## 
    eps = ""
    gam = ""
    for key, values in hashMap.items():

      if values[0] > values[1]:
        eps += "0"
        gam += "1"
      else:
        eps += "1"
        gam += "0"
    epsNum = int(eps, 2)
    gamNum = int(gam, 2)
    return epsNum * gamNum
  
  def filter(self, lines, index, isOxyRat):

    oneCount = 0
    zeroCount = 0

    for line in lines:
      if line[index] == '1':
        oneCount += 1
      else:
        zeroCount += 1 

    chosenVal = ""
    if isOxyRat:
      if oneCount >= zeroCount:
        chosenVal = '1'
      else:
        chosenVal = '0'
    else:
      if oneCount >= zeroCount:
        chosenVal = '0'
      else:
        chosenVal = '1'
      
    output = []
    for line in lines:
      if line[index] == chosenVal:
        output.append(line)
    return output

  def partTwo(self):

    ## Get Oxygen

    dataTemp = self.input.copy()
    index = 0
    size = len(dataTemp[0])

    while len(dataTemp) > 1:

      dataTemp = self.filter(dataTemp, index, True)
      index = (index + 1) % size
    oxyRat = int(dataTemp[0], 2)

    ## Get co2
    dataTemp = self.input.copy()
    index = 0
    
    while len(dataTemp) != 1:

      dataTemp = self.filter(dataTemp, index, False)
      index = (index + 1) % size

    coRat = int(dataTemp[0], 2)
    return oxyRat * coRat


if __name__ == "__main__":
  data = Read().createArray()
  Answers = Solution(data)
  print("Answer part 1 ", Answers.partOne())
  print("Answer part 2 ", Answers.partTwo())






