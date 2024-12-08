### Part 1

with open('testinput.txt', 'r') as file:
  lines = file.readlines()
  lines = [(line.rstrip()) for line in lines]

init, nums = lines[0].split(':')

initialState = nums.split(',')

for i in range(0, len(initialState)):
  initialState[i] = int(initialState[i])

print(initialState)


for i in range(0, 18):

  temp = []
  statesAdded = 0
  for i in range(0, len(initialState)):
    if initialState[i] == 0:
      statesAdded += 1
      temp.append(6)
    else:
      temp.append(initialState[i]-1)
  for i in range(0, statesAdded):
    temp.append(8)
  initialState = temp

print(len(initialState))


## Part 2
initialState = lines[0].split(',')
hashMap = defaultdict(int)
for i in range(0, len(initialState)):
    hashMap[int(initialState[i])] += 1


def helper(hashMap, days):
  h1 = hashMap
  for i in range(0, days):

    tempDic = defaultdict(int)

    for key, value in h1.items():
      if key == 0:
        tempDic[6] += value
        tempDic[8] += value
      else:
        tempDic[key-1] += value
    h1 = tempDic
    
  return sum(h1.values())


print(helper(hashMap, 256))
