def question(lines, part2=False) -> int:

  ans = 0
  # Splitting the input into separate grids
  for grid in lines.split('\n\n'):
      # Creating a 2D array (list of lists) from the grid
      graph = [list(row) for row in grid.split('\n')]
      row, col = len(graph), len(graph[0])

      # Processing columns
      for c in range(col - 1):
          bad = 0
          for delc in range(col):
              left, right = c - delc, c + delc + 1
              if 0 <= left < right < col:
                  for r in range(row):
                      if graph[r][left] != graph[r][right]:
                          bad += 1
          if (bad == 0 and not part2) or (bad == 1 and part2):
              ans += c + 1

      # Processing rows
      for r in range(row - 1):
          bad = 0
          for dr in range(row):
              up, down = r - dr, r + 1 + dr
              if 0 <= up < down < row:
                  for c in range(col):
                      if graph[up][c] != graph[down][c]:
                          bad += 1
          if (bad == 0 and not part2) or (bad == 1 and part2):
              ans += 100 * (r + 1)

  return ans

# Example usage
try:
  with open("input.txt", "r") as file:
      data = file.read().strip()
  print(question(data))
  print(question(data, True))
except FileNotFoundError:
  print("File not found. Please check the file path.")
except Exception as e:
  print(f"An error occurred: {e}")
