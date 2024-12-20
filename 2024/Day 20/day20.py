from collections import deque

def parse_grid(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)
    return rows, cols, start, end

def is_track(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    if 0 <= r < rows and 0 <= c < cols:
        return grid[r][c] in ('.', 'S', 'E')
    return False

def bfs_from_point(grid, start_cell):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    dist = [[None]*cols for _ in range(rows)]
    sr, sc = start_cell
    dist[sr][sc] = 0
    q = deque([start_cell])
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if is_track(grid, nr, nc) and dist[nr][nc] is None:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist

def solve_part1(grid):
    rows, cols, start, end = parse_grid(grid)
    dist_from_S = bfs_from_point(grid, start)
    dist_to_E = bfs_from_point(grid, end)

    normal_dist = dist_from_S[end[0]][end[1]]
    if normal_dist is None:
        return 0

    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    track_cells = [(r,c) for r in range(rows) for c in range(cols) if is_track(grid, r, c)]

    count_cheats = 0
    for sr, sc in track_cells:
        d_s = dist_from_S[sr][sc]
        if d_s is None:
            continue
        for dr1, dc1 in directions:
            ir, ic = sr+dr1, sc+dc1
            if 0 <= ir < rows and 0 <= ic < cols:
                for dr2, dc2 in directions:
                    er, ec = ir+dr2, ic+dc2
                    if 0 <= er < rows and 0 <= ec < cols and is_track(grid, er, ec):
                        d_e = dist_to_E[er][ec]
                        if d_e is not None:
                            cheated_time = d_s + 2 + d_e
                            saving = normal_dist - cheated_time
                            if saving >= 100:
                                count_cheats += 1

    return count_cheats

def solve_part2(grid):
    rows, cols, start, end = parse_grid(grid)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    dist_from_S = bfs_from_point(grid, start)
    dist_to_E = bfs_from_point(grid, end)

    normal_dist = dist_from_S[end[0]][end[1]]
    if normal_dist is None:
        return 0

    track_cells = [(r, c) for r in range(rows) for c in range(cols) if is_track(grid, r, c)]

    best_cheats = {}

    def cheat_bfs(start_cell):
        (sr, sc) = start_cell
        if dist_from_S[sr][sc] is None:
            return

        dist_ignoring_walls = [[None]*cols for _ in range(rows)]
        dist_ignoring_walls[sr][sc] = 0
        q = deque([(sr, sc)])
        while q:
            r, c = q.popleft()
            steps = dist_ignoring_walls[r][c]
            if steps == 20:
                continue
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dist_ignoring_walls[nr][nc] is None:
                        dist_ignoring_walls[nr][nc] = steps + 1
                        q.append((nr, nc))

        d_s = dist_from_S[sr][sc]
        for r in range(rows):
            for c in range(cols):
                steps = dist_ignoring_walls[r][c]
                if steps is not None and is_track(grid, r, c):
                    d_e = dist_to_E[r][c]
                    if d_s is not None and d_e is not None:
                        cheated_time = d_s + steps + d_e
                        saving = normal_dist - cheated_time
                        if saving > 0:
                            key = ((sr, sc), (r, c))
                            if key not in best_cheats or best_cheats[key] < saving:
                                best_cheats[key] = saving

    for cell in track_cells:
        cheat_bfs(cell)

    count = sum(1 for s in best_cheats.values() if s >= 100)
    return count

if __name__ == "__main__":
    # Replace this with your input file
    with open(r"C:\\Users\\<redact>\\OneDrive\\Documents\\AdventOfCode\\2024\\input.txt", "r") as f:
        puzzle_input = [line.rstrip('\n') for line in f]

    # Run both parts
    part1_result = solve_part1(puzzle_input)
    part2_result = solve_part2(puzzle_input)

    print("Part 1 result:", part1_result)
    print("Part 2 result:", part2_result)
