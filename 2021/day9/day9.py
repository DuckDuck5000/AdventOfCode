with open('input.txt', 'r') as file:
  lines = file.readlines()
  lines = [list(line.rstrip()) for line in lines]
  
matrix = []

for line in lines:

  matrix.append(list(line))

for i in range(0, len(matrix)):
  for j in range(0, len(matrix[0])):

    matrix[i][j] = int(matrix[i][j])

def isLowNum(matrix, i, j):

    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for delX, delY in directions:
      
      newX = i + delX
      newY = j + delY

      if newX >= 0 and newX < len(matrix) and newY >= 0 and newY < len(matrix[0]) and matrix[newX][newY] <= matrix[i][j]:
          return False
    return True
  
## Part 1: find low points

lowPoints = 0
for i in range(0, len(matrix)):
  for j in range(0, len(matrix[0])):

      if isLowNum(matrix, i, j):
        lowPoints += matrix[i][j] + 1
print("Part 1 ", lowPoints)


## Part 2: Find basins
visited = set()
basins = []
for i in range(0, len(matrix)):
  for j in range(0, len(matrix[i])):

    if (i,j) not in visited and matrix[i][j] != 9:
      q = [(i,j)]
      size = 0
      while q:
        x, y = q.pop(0)
        if (x,y) not in visited:
          visited.add((x,y))
          size += 1
          for delX, delY in [[-1,0], [1, 0], [0, 1], [0, -1]]:

            newX = x + delX
            newY = y + delY

            ## bound check
            if newX >= 0 and newX < len(matrix) and newY >= 0 and newY < len(matrix[0]) and matrix[newX][newY] != 9:
              q.append((newX, newY))
      basins.append(size)
basins.sort()

## Only concerned about 3 largest bain,
print(basins[-1]*basins[-2]*basins[-3])

