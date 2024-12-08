import math
from itertools import combinations
from collections import defaultdict

def count_unique_antinode_locations_part1(grid):
    
    nrows = len(grid)
    if nrows == 0:
        return 0
    ncols = len(grid[0])

    antennas = defaultdict(list)
    for row in range(nrows):
        line = grid[row]
        for col in range(ncols):
            char = line[col]
            if char != '.':
                antennas[char].append((col, row))

    antinode_set = set()

    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue  

        for A, B in combinations(positions, 2):

            C1_col = 2 * B[0] - A[0]
            C1_row = 2 * B[1] - A[1]
            if 0 <= C1_col < ncols and 0 <= C1_row < nrows:
                antinode_set.add((C1_col, C1_row))

            C2_col = 2 * A[0] - B[0]
            C2_row = 2 * A[1] - B[1]
            if 0 <= C2_col < ncols and 0 <= C2_row < nrows:
                antinode_set.add((C2_col, C2_row))

    return len(antinode_set)


def count_unique_antinode_locations_part2(grid):
    nrows = len(grid)
    if nrows == 0:
        return 0
    ncols = len(grid[0])

    antennas = defaultdict(list)
    for y in range(nrows):
        line = grid[y]
        for x in range(ncols):
            char = line[x]
            if char != '.':
                antennas[char].append((x, y))

    antinode_set = set()

    def get_line_positions(p1, p2, ncols, nrows):
        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1

        if dx == 0 and dy == 0:
            return {(x1, y1)}
        
        gcd_val = math.gcd(abs(dx), abs(dy))
        if gcd_val == 0:
            return set()

        step_x = dx // gcd_val
        step_y = dy // gcd_val

        positions = set()

        # Step forward from p1
        x, y = x1, y1
        while 0 <= x < ncols and 0 <= y < nrows:
            positions.add((x, y))
            x += step_x
            y += step_y

        x, y = x1 - step_x, y1 - step_y
        while 0 <= x < ncols and 0 <= y < nrows:
            positions.add((x, y))
            x -= step_x
            y -= step_y

        return positions

    for freq, positions in antennas.items():
        if len(positions) < 2:
            continue  
        
        for p1, p2 in combinations(positions, 2):
            line_positions = get_line_positions(p1, p2, ncols, nrows)
            antinode_set.update(line_positions)

    return len(antinode_set)


grid = [line.strip() for line in  open('C:\\Users\\<redacted>\\OneDrive\\Documents\\AdventOfCode\\2024\\Day 8\\input.txt', 'r') if line.strip()]

part1 = count_unique_antinode_locations_part1(grid)
part2 = count_unique_antinode_locations_part2(grid)
print(part1, part2) 
