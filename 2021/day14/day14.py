'''
lines = []
folds = []
maxY = 0
maxX = 0
problem1 = True
graph1 = {}
graph2 = {}

origString = []
pairDict = {}
for line in  open('input.txt', 'r'):
  line = line.strip().split('->')

  if len(line) == 1:
    origString.append(line)
    origString = origString[0]
  else:
    pairDict[line[0].strip()] = line[1].strip()
print(pairDict)



steps = 0
print(origString)
'''
'''
while steps < 40:
  newString = ""

  for i in range(0, len(origString)-1):

    if origString[i:i+2] in pairDict:
      newString += origString[i]
      newString += pairDict[origString[i:i+2]]
    if i == len(origString)-2:
      newString += origString[i+1]

  steps += 1
  origString = newString
'''


print(origString)

