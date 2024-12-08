from itertools import product
from collections import deque

def expand_universe(grid):
    empty_rows = {i for i, row in enumerate(grid) if '#' not in row}
    empty_cols = {j for j in range(len(grid[0])) if all(grid[i][j] != '#' for i in range(len(grid)))}

    new_grid = []
    for i, row in enumerate(grid):
        new_row = ''.join(cell + (cell if j in empty_cols else '') for j, cell in enumerate(row))
        new_grid.append(new_row)
        if i in empty_rows:
            new_grid.append(new_row)
    return new_grid

def assign_galaxies(grid):
    galaxy_positions = {}
    galaxy_number = 1
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '#':
                galaxy_positions[galaxy_number] = (i, j)
                galaxy_number += 1
    return galaxy_positions

def bfs_preprocess(grid, start):
    queue = deque([(start, 0)])
    distances = {}
    visited = set([start])
    while queue:
        (x, y), dist = queue.popleft()
        distances[(x, y)] = dist
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))
    return distances

def sum_shortest_paths(grid):
    expanded_grid = expand_universe(grid)
    galaxy_positions = assign_galaxies(expanded_grid)
    shortest_paths = {g: bfs_preprocess(expanded_grid, pos) for g, pos in galaxy_positions.items()}

    total_distance = 0
    for galaxy1, galaxy2 in product(galaxy_positions.keys(), repeat=2):
        if galaxy1 < galaxy2:
            distance = shortest_paths[galaxy1][galaxy_positions[galaxy2]]
            total_distance += distance

    return total_distance


## part 2

def count_empty_rows_and_columns(grid):
  empty_rows = {i for i, row in enumerate(grid) if '#' not in row}
  empty_cols = {j for j in range(len(grid[0])) if all(grid[i][j] != '#' for i in range(len(grid)))}
  return empty_rows, empty_cols

def calculate_effective_distance(grid, start, end, empty_rows, empty_cols):
  x1, y1 = start
  x2, y2 = end

  distance = abs(x1 - x2) + abs(y1 - y2)

  if x1 != x2:
      row_range = range(min(x1, x2), max(x1, x2))
      distance += sum(1 for i in row_range if i in empty_rows) * (1000000 - 1)
  if y1 != y2:
      col_range = range(min(y1, y2), max(y1, y2))
      distance += sum(1 for j in col_range if j in empty_cols) * (1000000 - 1)

  return distance

def sum_effective_shortest_paths(grid):
  galaxy_positions = assign_galaxies(grid)
  empty_rows, empty_cols = count_empty_rows_and_columns(grid)

  total_distance = 0
  for (galaxy1, pos1), (galaxy2, pos2) in product(galaxy_positions.items(), repeat=2):
      if galaxy1 < galaxy2:
          distance = calculate_effective_distance(grid, pos1, pos2, empty_rows, empty_cols)
          total_distance += distance

  return total_distance

# Read the file and process it
file_path = "input.txt"
with open(file_path, "r") as file:
    input_grid = [line.strip() for line in file]

print(sum_shortest_paths(input_grid))
print(sum_effective_shortest_paths(input_grid))
