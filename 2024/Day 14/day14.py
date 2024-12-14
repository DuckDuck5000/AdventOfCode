import re
from collections import deque

# Grid dimensions
WIDTH = 101
HEIGHT = 103

# Middle lines
MID_X = 50
MID_Y = 51


robots = []
pattern = re.compile(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)")
with open("C:\\Users\\cdrec\\OneDrive\\Documents\\AdventOfCode\\2024\\input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        match = pattern.search(line)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            dx = int(match.group(3))
            dy = int(match.group(4))
            robots.append((x, y, dx, dy))

# Simulate after 100 seconds
TIME = 100
final_positions = []
for (x, y, dx, dy) in robots:
    # New position after 100 seconds
    new_x = (x + dx * TIME) % WIDTH
    new_y = (y + dy * TIME) % HEIGHT
    final_positions.append((new_x, new_y))

# Count robots in each quadrant
# Quadrants:
# Q1: x<50, y<51 (top-left)
# Q2: x>50, y<51 (top-right)
# Q3: x<50, y>51 (bottom-left)
# Q4: x>50, y>51 (bottom-right)
q1 = q2 = q3 = q4 = 0

for (x, y) in final_positions:
    if x == MID_X or y == MID_Y:
        # on dividing line, don't count
        continue
    if x < MID_X and y < MID_Y:
        q1 += 1
    elif x > MID_X and y < MID_Y:
        q2 += 1
    elif x < MID_X and y > MID_Y:
        q3 += 1
    elif x > MID_X and y > MID_Y:
        q4 += 1

# Safety factor
safety_factor = q1 * q2 * q3 * q4
print(safety_factor)

def positions_at_time(t):
    """Return list of (x,y) positions of all robots at time t."""
    return [(x + dx*t, y + dy*t) for (x, y, dx, dy) in robots]

def bounding_area(positions):
    """Compute the bounding box area given a list of positions."""
    xs = [p[0] for p in positions]
    ys = [p[1] for p in positions]
    width = max(xs) - min(xs)
    height = max(ys) - min(ys)
    area = width * height
    return area, (min(xs), max(xs), min(ys), max(ys))

# Define the grid based on final positions
G = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
for x, y in final_positions:
    G[y][x] = '#'

# Count connected components in the grid
components = 0
seen = set()

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, right, down, left

def bfs(start_x, start_y):
    """Perform BFS to explore a connected component."""
    queue = deque([(start_x, start_y)])
    while queue:
        x, y = queue.popleft()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for dx, dy in DIRS:
            neighbor_x, neighbor_y = x + dx, y + dy
            if (0 <= neighbor_x < WIDTH and 0 <= neighbor_y < HEIGHT and
                G[neighbor_y][neighbor_x] == '#' and (neighbor_x, neighbor_y) not in seen):
                queue.append((neighbor_x, neighbor_y))

for x in range(WIDTH):
    for y in range(HEIGHT):
        if G[y][x] == '#' and (x, y) not in seen:
            components += 1
            bfs(x, y)

print(f"Connected components: {components}")
