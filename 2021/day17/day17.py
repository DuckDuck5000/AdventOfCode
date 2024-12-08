'''
import heapq
import math

lines = []

for line in open('input.txt'):
  lines.append(line)

## part 1
costs = []

for line in lines:
  costs.append(list(map(int, line.strip())))

dp = [[float('inf')]*len(costs) for _ in costs]
dp[0][0] = 0
q = []
heapq.heappush()




def solve(risks):
    bests = [[math.inf] * len(row) for row in risks]
    bests[0][0] = 0
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    while True:
        _, x0, y0 = heapq.heappop(queue)
        c = bests[y0][x0]
        if y0 == len(risks) - 1 and x0 == len(risks[y0]) - 1:
            return c
        for x1, y0 in ((x0 - 1, y0), (x0, y0 - 1), (x0, y0 + 1), (x0 + 1, y0)):
            if y0 not in range(len(risks)) or x1 not in range(len(risks[y0])):
                continue
            d = c + risks[y0][x1]
            if d < bests[y0][x1]:
                bests[y0][x1] = d
                heapq.heappush(queue, (d, x1, y0))


def part1(lines):
    risks = [list(map(int, line.strip())) for line in lines]
    return solve(risks)


def part2(lines):
    """
    >>> part2(SAMPLE_INPUT)
    315
    """
    risks = [
        [(int(char) - 1 + dx + dy) % 9 + 1 for dx in range(5) for char in line.strip()]
        for dy in range(5)
        for line in lines
    ]
    return solve(risks)


parts = (part1, part2)
print(part1(lines))
print(part2(lines))
'''

lines = []
for line in open("input.txt", "r"):
    #lines.append(line)
    line = line.split("=")
    xCoords = line[1].split("..")
    yCoords = line[-1].split("..")

    y = xCoords[1][:-3]
    print(line)
    print(xCoords)
    print(yCoords)
    print(y)

import time
part1 = 0
partTwo = 0
start = time.time()
for currX in range(0, 300):
  for currY in range(-100, 500):

    goodMoves = False
    x = 0
    y = 0
    dx = currX
    dy = currY
    maxY = -float('inf')

    for j in range(0, 1000):

      x += dx
      y += dy

      maxY = max(maxY, y)

      if dx > 0:
        dx -= 1
      elif dx < 0:
        dx += 1
      dy -= 1

      if int(xCoords[0])<= x <=int(xCoords[1][:-3]) and int(yCoords[0]) <= y <= int(yCoords[1]):
        goodMoves = True
    if goodMoves:
      partTwo += 1
      if maxY > part1:
        part1 = maxY
    #print(part1)
print(part1) 
print(partTwo)
print("Total time:", time.time()-start)
