
with open('input.txt') as file:
    lines = file.readlines()
    lines = [(line.rstrip()) for line in lines]

hashMap = {}
totalLines = len(lines)
eps = ""
gam = ""


### Part 1

for i in range(0, 12):
  hashMap[i] = [0, 0]

for line in lines:
  line = str(line)
  for i in range(0, len(line)):
    if int(line[i]) == 0:
      hashMap[i][0] += 1
    else:
      hashMap[i][1] += 1

eps = ""
gam = ""


for key, values in hashMap.items():

  if values[0] > values[1]:
    eps += str(0)
    gam += str(1)
  else:
    eps += str(1)
    gam += str(0)
print("gam", gam)
print("eps", eps)
epsNum = int(eps, 2)
gamNum = int(gam, 2)

print("epsNum", epsNum)
print("gamNum", gamNum)

print(epsNum*gamNum)







### Part 2
print(hashMap)
lines2 = lines.copy()
while len(lines) > 1:
  ## initialize hash

  for i in range(0, 12):
    hashMap[i] = [0, 0]

  for line in lines:
    line = str(line)
    for i in range(0, len(line)):
      if int(line[i]) == 0:
        hashMap[i][0] += 1
      else:
        hashMap[i][1] += 1
  
  for index in range(0, 12):
    print("Lines", lines)
        ## reinitilizae hashMap
    for i in range(0, 12):
      hashMap[i] = [0, 0]
    for line in lines:
      line = str(line)
      for i in range(0, len(line)):
        if int(line[i]) == 0:
          hashMap[i][0] += 1
        else:
          hashMap[i][1] += 1
    values = hashMap[index]
    print("Values", values)
    if values[0] > values[1]:
      temp = []
      for line in lines:
        if line[index] == "0":
          temp.append(line)
      lines = temp
    else:
      temp = []
      for line in lines:
        if line[index] == "1":
          temp.append(line)
      lines = temp
  
co2 = ''
o2 = lines[0]

while len(lines2) > 1:
  ## initialize hash
  for i in range(0, 12):
    hashMap[i] = [0, 0]

  for line in lines2:
    line = str(line)
    for i in range(0, len(line)):
      if int(line[i]) == 0:
        hashMap[i][0] += 1
      else:
        hashMap[i][1] += 1
  
  for index in range(0, 12):
    
        ## reinitilizae hashMap
    for i in range(0, 12):
      hashMap[i] = [0, 0]
    for line in lines2:
      line = str(line)
      for i in range(0, len(line)):
        if int(line[i]) == 0:
          hashMap[i][0] += 1
        else:
          hashMap[i][1] += 1
    values = hashMap[index]
    print("hashMap", hashMap)
    if values[0] <= values[1]:
      temp = []
      print("Her")
      for line in lines2:
        if line[index] == "0":
          temp.append(line)
      lines2 = temp
    else:
      temp = []
      for line in lines2:
        if line[index] == "1":
          temp.append(line)
      lines2 = temp
    
    if len(lines2) == 1:
      break
    
print(lines2)
print(lines)

num1 = int(lines2[0], 2)
num2 = int(lines[0], 2)

print(num1*num2)
