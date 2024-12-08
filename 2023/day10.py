 def read_grid(file_path):
  with open(file_path, "r") as file:
      return [line.strip() for line in file]

def find_start_position(grid):
  for i, row in enumerate(grid):
      if "S" in row:
          return i, row.find("S")
  return -1, -1

def get_initial_directions(grid, start_x, start_y):
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  valid_connections = ["-7J", "|LJ", "-FL", "|F7"]
  valid_dirs = []
  for i, (dx, dy) in enumerate(directions):
      nx, ny = start_x + dx, start_y + dy
      if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] in valid_connections[i]:
          valid_dirs.append(i)
  return valid_dirs

def calculate_loop_length(grid, start_x, start_y, directions):
  transform = {
      (0, "-"): 0, (0, "7"): 1, (0, "J"): 3,
      (2, "-"): 2, (2, "F"): 1, (2, "L"): 3,
      (1, "|"): 1, (1, "L"): 0, (1, "J"): 2,
      (3, "|"): 3, (3, "F"): 0, (3, "7"): 2,
  }
  dir_sequence = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  current_dir = directions[0]
  x, y = start_x + dir_sequence[current_dir][0], start_y + dir_sequence[current_dir][1]
  length = 1
  visited = set()
  visited.add((start_x, start_y))
  while (x, y) != (start_x, start_y):
      visited.add((x, y))
      length += 1
      current_dir = transform[(current_dir, grid[x][y])]
      x, y = x + dir_sequence[current_dir][0], y + dir_sequence[current_dir][1]
  return length, visited

def count_internal_spaces(grid, visited, start_valid):
  count = 0
  for i, row in enumerate(grid):
      inside = False
      for j, cell in enumerate(row):
          if (i, j) in visited:
              if cell in "|JL" or (cell == "S" and start_valid):
                  inside = not inside
          else:
              count += inside
  return count

def main(file_path):
  try:
      grid = read_grid(file_path)
      start_x, start_y = find_start_position(grid)
      if start_x == -1:
          print("Start position not found")
          return

      initial_dirs = get_initial_directions(grid, start_x, start_y)
      start_valid = 3 in initial_dirs  # Check if starting position is valid

      loop_length, visited = calculate_loop_length(grid, start_x, start_y, initial_dirs)
      print("Loop Length:", loop_length)

      internal_spaces = count_internal_spaces(grid, visited, start_valid)
      print("Internal Spaces:", internal_spaces)

  except FileNotFoundError:
      print(f"File not found: {file_path}")
  except Exception as e:
      print(f"An error occurred: {e}")

# Usage
file_path = "input.txt"
main(file_path)
