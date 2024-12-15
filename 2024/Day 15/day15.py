import sys
import re
from collections import deque


DIRECTIONS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def parse_ints(s):
    return [int(x) for x in re.findall(r'-?\d+', s)]

def solve(grid_lines, instructions, part2=False):

    rows = len(grid_lines)
    cols = len(grid_lines[0])
    grid = [list(row) for row in grid_lines]

    # Part 2 transformation: each cell is doubled horizontally.
    if part2:
        transformed = []
        for r in range(rows):
            new_row = []
            for c in range(cols):
                ch = grid[r][c]
                if ch == '#':
                    new_row.extend(['#', '#'])
                elif ch == 'O':
                    new_row.extend(['[', ']'])
                elif ch == '.':
                    new_row.extend(['.', '.'])
                elif ch == '@':
                    new_row.extend(['@', '.'])
            transformed.append(new_row)
        grid = transformed
        cols *= 2

    start_r = start_c = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                start_r, start_c = r, c
                grid[r][c] = '.' 
                break
        if start_r is not None:
            break

    robot_r, robot_c = start_r, start_c

    for inst in instructions:
        if inst == '\n':
            continue
        dr, dc = DIRECTIONS[inst]
        next_r = robot_r + dr
        next_c = robot_c + dc

        if grid[next_r][next_c] == '#':
            continue

        cell = grid[next_r][next_c]
        if cell == '.':
            robot_r, robot_c = next_r, next_c
        elif cell in ['[', ']', 'O']:
            if try_push_boxes(grid, robot_r, robot_c, dr, dc):
                robot_r, robot_c = next_r, next_c
            else:
                continue

    return compute_gps_sum(grid)

def try_push_boxes(grid, robot_r, robot_c, dr, dc):

    start_r = robot_r + dr
    start_c = robot_c + dc

    rows = len(grid)
    cols = len(grid[0])

    queue = deque([(start_r, start_c)])
    seen = set()
    push_possible = True

    while queue:
        rr, cc = queue.popleft()
        if (rr, cc) in seen:
            continue
        seen.add((rr, cc))
        target_r = rr + dr
        target_c = cc + dc

        if target_r < 0 or target_r >= rows or target_c < 0 or target_c >= cols:
            push_possible = False
            break
        if grid[target_r][target_c] == '#':
            push_possible = False
            break

        if grid[target_r][target_c] in ['[', ']', 'O']:
            queue.append((target_r, target_c))

    if not push_possible:
        return False

    while seen:
        moved_any = False
        for rr, cc in sorted(seen):
            target_r = rr + dr
            target_c = cc + dc
            
            if grid[target_r][target_c] == '.':
                grid[target_r][target_c] = grid[rr][cc]
                grid[rr][cc] = '.'
                seen.remove((rr, cc))
                moved_any = True
                break
        if not moved_any:
            break

    return True

def compute_gps_sum(grid):
    rows = len(grid)
    cols = len(grid[0])
    total = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ['[', 'O']:
                total += 100 * r + c
    return total

def main():
    infile = "C:\\Users\\<redact>\\OneDrive\\Documents\\AdventOfCode\\2024\\input.txt"
    data = open(infile).read().strip()
    grid_data, instructions = data.split('\n\n')
    grid_lines = grid_data.split('\n')

    result_part1 = solve(grid_lines, instructions, part2=False)
    print(result_part1)
    result_part2 = solve(grid_lines, instructions, part2=True)
    print(result_part2)

if __name__ == "__main__":
    main()
