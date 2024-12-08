
with open('input.txt', 'r') as file:
  lines = file.readlines()
  lines = [(line.rstrip()) for line in lines]



nums = lines[0].split(',')

boards = []
rows = {}
cols = {}
visited = {}
i = 2
k = 0
while i <= len(lines):

  board = []
  for j in range(i, i+5):
    board.append(lines[j].split())
  boards.append(board)
  cols[k] = {}
  rows[k] = {}
  visited[k] = [[False for _ in range(0, len(boards[0]))] for _ in range(0, len(boards[0]))]
  for l in range(0, len(board)):
    cols[k][l] = 0
    rows[k][l] = 0

  
  k += 1
  i += 6

targetSum = len(boards[0])
stillLooking = True
boardsWon = [False for _ in range(0, len(boards))]
for num in nums:

  if stillLooking:
    for k in range(0, len(boards)):

      for i in range(0, len(boards[k])):
        for j in range(0, len(boards[k][i])):

          if boards[k][i][j] == num:
            rows[k][j] += 1
            cols[k][i] += 1
            visited[k][i][j] = True

            if cols[k][i] == targetSum:
              boardsWon[k] = True
              if sum(boardsWon) == len(boards):
                ## last one
                
                tempSum = 0
                ## find sum 
                for x in range(0, len(boards[k])):
                  for y in range(0, len(boards[k][x])):
                    if visited[k][x][y] == False:
                      tempSum += int(boards[k][x][y])
                stillLooking = False
                print("This is the answer ", tempSum * int(num))
              
            if rows[k][j] == targetSum:
              boardsWon[k] = True
              if sum(boardsWon) == len(boards):
                tempSum = 0
              ## find sum 
                for x in range(0, len(boards[k])):
                  for y in range(0, len(boards[k][x])):
                    if visited[k][x][y] == False:
                      print("Adding ", boards[k][x][y])
                      tempSum += int(boards[k][x][y])
                  print("TempSum ", tempSum)
                stillLooking = False
                print("This is the answer ", tempSum * int(num))










