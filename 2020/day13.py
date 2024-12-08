rawInput = []
with open('input.txt', 'r') as file:
  rawInput.append(file.read().splitlines())
busses = [rawInput[0][1].split(",")]
earliestTime = int(rawInput[0][0])
busNum = []
for i in busses[0]:
  if i != 'x':
    busNum.append(int(i))


tempMin = 0
times = {}
for i in busNum:
  if earliestTime % i == 0:
    print(0)
  else:
    tempMin = (i- earliestTime%i)
    times[i] = tempMin

result = min(times.items(), key=lambda x: x[1])
print(result[0]* result[1])

## Part 2

data = open('input.txt', 'r').read().split('\n')
data = data[1].split(',')
B = [(int(data[k]), k) for k in range(len(data)) if data[k] != 'x']

lcm = 1
time = 0    
for i in range(len(B)-1):
	bus_id = B[i+1][0]
	idx = B[i+1][1]
	lcm *= B[i][0]
	while (time + idx) % bus_id != 0:
		time += lcm
print(time)
    

  
