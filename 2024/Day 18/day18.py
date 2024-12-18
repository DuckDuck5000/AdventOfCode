from collections import deque

def read_coordinates(filename, count=None):
    with open(filename, 'r') as f:
        coords = (line.strip().split(',') for line in f)
        for parts in coords:
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                yield (int(parts[0]), int(parts[1]))
                if count is not None:
                    count -= 1
                    if count == 0:
                        break

def bfs_path(grid, goal):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * 71 for _ in range(71)]
    queue = deque([(0, 0, 0)]) 
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == goal:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 71 and 0 <= ny < 71 and not visited[ny][nx] and not grid[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, dist + 1))
    return None

def part1(grid, coords):
    for x, y in coords:
        grid[y][x] = True
    return bfs_path(grid, (70, 70))

def part2(grid, coords):
    for x, y in coords:
        grid[y][x] = True
        if bfs_path(grid, (70, 70)) is None:
            return x, y
    return None

def main():
    maze_path = r"C:\\Users\\<redact>\\OneDrive\\Documents\\AdventOfCode\\2024\\input.txt"
    grid = [[False] * 71 for _ in range(71)]


    coords_1024 = list(read_coordinates(maze_path, count=1024))
    shortest_path_steps = part1(grid, coords_1024)
    print(f"Part 1: The minimum number of steps needed to reach the exit is: {shortest_path_steps}")

    grid = [[False] * 71 for _ in range(71)] 
    coords_all = read_coordinates(maze_path)
    blocking_byte = part2(grid, coords_all)
    print(f"Part 2: The first byte that blocks the path is at: {blocking_byte[0]},{blocking_byte[1]}")

main()
