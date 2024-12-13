import sys
from collections import deque

# Read grid from input.txt
grid = [line.strip() for line in open('input.txt', 'r') if line.strip()]

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

def calculate_perimeter_and_sides(grid):
    R, C = len(grid), len(grid[0])
    seen = set()
    p1 = 0
    p2 = 0

    for r in range(R):
        for c in range(C):
            if (r, c) in seen:
                continue
            area = 0
            perim = 0
            sides = 0
            region = set()
            q = deque([(r, c)])

            while q:
                r2, c2 = q.popleft()
                if (r2, c2) in region:
                    continue
                region.add((r2, c2))
                area += 1
                for dr, dc in DIRS:
                    rr, cc = r2 + dr, c2 + dc
                    if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == grid[r2][c2]:
                        q.append((rr, cc))
                    else:
                        perim += 1

            corner_candidates = set()
            for r2, c2 in region:
                for cr, cc in [(r2 - 0.5, c2 - 0.5), (r2 + 0.5, c2 - 0.5), (r2 + 0.5, c2 + 0.5), (r2 - 0.5, c2 + 0.5)]:
                    corner_candidates.add((cr, cc))

            for cr, cc in corner_candidates:
                config = [(sr, sc) in region for sr, sc in [(cr - 0.5, cc - 0.5), (cr + 0.5, cc - 0.5), (cr + 0.5, cc + 0.5), (cr - 0.5, cc + 0.5)]]
                count = sum(config)
                if count == 1:
                    sides += 1
                elif count == 2 and config in ([True, False, True, False], [False, True, False, True]):
                    sides += 2
                elif count == 3:
                    sides += 1

            p1 += area * perim
            p2 += area * sides
            seen.update(region)

    return p1, p2

p1, p2 = calculate_perimeter_and_sides(grid)
print(p1)
print(p2)
