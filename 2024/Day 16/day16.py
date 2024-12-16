import sys
import re
import heapq
from collections import deque


def pr(s):
    print(s)


DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)] 

def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

def read_maze(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read().strip()
    except FileNotFoundError:
        pr(f"Error: The file at {file_path} was not found.")
        sys.exit(1)
    except Exception as e:
        pr(f"An error occurred while reading the file: {e}")
        sys.exit(1)

    lines = data.split('\n')
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    maze = [[lines[r][c] for c in range(cols)] for r in range(rows)]
    return maze, rows, cols

def find_start_end(maze, rows, cols):
    start = end = (-1, -1)
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    if start == (-1, -1) or end == (-1, -1):
        pr("Error: Maze must have exactly one Start (S) and one End (E) position.")
        sys.exit(1)
    return start, end

def dijkstra(maze, rows, cols, start, end):
    heap = []
    sr, sc = start
    er, ec = end
  
    heapq.heappush(heap, (0, sr, sc, 1))

    DIST = {}  
    while heap:
        cost, r, c, dir_idx = heapq.heappop(heap)

        if (r, c, dir_idx) in DIST:
            if DIST[(r, c, dir_idx)] <= cost:
                continue
        DIST[(r, c, dir_idx)] = cost

        
        if (r, c) == end:
            return cost, DIST

       
        dr, dc = DIRS[dir_idx]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
            new_cost = cost + 1
            if (nr, nc, dir_idx) not in DIST or new_cost < DIST.get((nr, nc, dir_idx), float('inf')):
                heapq.heappush(heap, (new_cost, nr, nc, dir_idx))

        new_dir = (dir_idx - 1) % 4
        new_cost = cost + 1000
        if (r, c, new_dir) not in DIST or new_cost < DIST.get((r, c, new_dir), float('inf')):
            heapq.heappush(heap, (new_cost, r, c, new_dir))

        new_dir = (dir_idx + 1) % 4
        new_cost = cost + 1000
        if (r, c, new_dir) not in DIST or new_cost < DIST.get((r, c, new_dir), float('inf')):
            heapq.heappush(heap, (new_cost, r, c, new_dir))

    return -1, DIST

def reverse_dijkstra(maze, rows, cols, start, end):
    heap = []
    er, ec = end
    
    for dir_idx in range(4):
        heapq.heappush(heap, (0, er, ec, dir_idx))

    DIST2 = {}  
    while heap:
        cost, r, c, dir_idx = heapq.heappop(heap)

        if (r, c, dir_idx) in DIST2:
            if DIST2[(r, c, dir_idx)] <= cost:
                continue
        DIST2[(r, c, dir_idx)] = cost

        opposite_dir = (dir_idx + 2) % 4
        dr, dc = DIRS[opposite_dir]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
            new_cost = cost + 1
            if (nr, nc, dir_idx) not in DIST2 or new_cost < DIST2.get((nr, nc, dir_idx), float('inf')):
                heapq.heappush(heap, (new_cost, nr, nc, dir_idx))

        new_dir = (dir_idx - 1) % 4
        new_cost = cost + 1000
        if (r, c, new_dir) not in DIST2 or new_cost < DIST2.get((r, c, new_dir), float('inf')):
            heapq.heappush(heap, (new_cost, r, c, new_dir))

        new_dir = (dir_idx + 1) % 4
        new_cost = cost + 1000
        if (r, c, new_dir) not in DIST2 or new_cost < DIST2.get((r, c, new_dir), float('inf')):
            heapq.heappush(heap, (new_cost, r, c, new_dir))

    return DIST2

def count_best_path_tiles(dist, dist2, best_cost):

    best_tiles = set()
    for (r, c, dir_idx), cost1 in dist.items():
        cost2 = dist2.get((r, c, dir_idx), float('inf'))
        if cost1 + cost2 == best_cost:
            best_tiles.add((r, c))
    return best_tiles

def mark_maze(maze, tiles):

    for r, c in tiles:
        if maze[r][c] not in ('S', 'E'):
            maze[r][c] = 'O'
    return maze

def print_maze(maze):

    for row in maze:
        print(''.join(row))

def main():

    # File path to the maze input
    maze_path = r"C:\Users\<redcated>\OneDrive\Documents\AdventOfCode\2024\input.txt"

    # Read and parse the maze
    maze, rows, cols = read_maze(maze_path)
    start, end = find_start_end(maze, rows, cols)

    # First Dijkstra's search: from Start to End
    best_cost, dist = dijkstra(maze, rows, cols, start, end)
    if best_cost == -1:
        pr("No path found from Start (S) to End (E).")
        sys.exit(0)
    pr(f"Lowest score: {best_cost}")

    # Second Dijkstra's search: from End to all positions
    dist2 = reverse_dijkstra(maze, rows, cols, start, end)

    best_tiles = count_best_path_tiles(dist, dist2, best_cost)
    pr(f"Number of tiles on any best path: {len(best_tiles)}")

    maze_marked = mark_maze(maze, best_tiles)
    pr("\nMaze with best path tiles marked as 'O':\n")
    print_maze(maze_marked)

if __name__ == "__main__":
    main()
