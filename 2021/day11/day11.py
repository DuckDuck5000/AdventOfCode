matrix = []
for line in  open('input.txt', 'r'):
  matrix.append([int(x) for x in line.rstrip()])


totalFlash = 0
def helper(i,j):
    global totalFlash
    totalFlash += 1
    matrix[i][j] = -1
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            newX = i+dx
            newY = j+dy
            if 0<=newX<len(matrix) and 0<=newY<len(matrix[0]) and matrix[newX][newY]!=-1:
                matrix[newX][newY] += 1
                if matrix[newX][newY] >= 10:
                    helper(newX,newY)

timer = 0
while done:
    timer += 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] += 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 10:
                helper(i,j)
    done = True
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
            else:
                done = False
    if timer == 100:
        print(totalFlash)
    if done:
        print(timer)
        break
