def solve_part1(grid):
    n = len(grid)
    m = len(grid[0])
    grid = [list(row) for row in grid]

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_map = {'^': 0, '>': 1, 'v': 2, '<': 3}

    start_x, start_y, direction = None, None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] in dir_map:
                start_x, start_y = i, j
                direction = dir_map[grid[i][j]]
                grid[i][j] = '.'  
                break
        if start_x is not None:
            break

    visited = set()
    visited.add((start_x, start_y))
    x, y = start_x, start_y

    while True:
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == '#':
                direction = (direction + 1) % 4
            else:
                x, y = nx, ny
                visited.add((x, y))
        else:
            break

    return len(visited)

grid_example = [...]
result_part1 = solve_part1(grid_example)
print("Part 1 result:", result_part1)


def solve_part2(grid):
    start_time = time.perf_counter()

    n = len(grid)
    m = len(grid[0])
    grid = [list(row) for row in grid]

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_map = {'^': 0, '>': 1, 'v': 2, '<': 3}

    start_x, start_y, start_dir = None, None, None
    for i in range(n):
        for j in range(m):
            if grid[i][j] in dir_map:
                start_x, start_y = i, j
                start_dir = dir_map[grid[i][j]]
                grid[i][j] = '.'  
                break
        if start_x is not None:
            break

    def simulate(extra_obstacle=None):
        if extra_obstacle:
            ox, oy = extra_obstacle
            saved_char = grid[ox][oy]
            grid[ox][oy] = '#'
        else:
            saved_char = None

        x, y = start_x, start_y
        d = start_dir
        visited_states = set()
        visited_states.add((x, y, d))

        while True:
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < m):
                if extra_obstacle:
                    grid[extra_obstacle[0]][extra_obstacle[1]] = saved_char
                return 'exit'
            else:
                if grid[nx][ny] == '#':
                    d = (d + 1) % 4
                else:
                    x, y = nx, ny
                    state = (x, y, d)
                    if state in visited_states:
                        if extra_obstacle:
                            grid[extra_obstacle[0]][extra_obstacle[1]] = saved_char
                        return 'loop'
                    visited_states.add(state)

    loop_positions = []
    for i in range(n):
        for j in range(m):
            if (i, j) != (start_x, start_y) and grid[i][j] == '.':
                result = simulate((i, j))
                if result == 'loop':
                    loop_positions.append((i, j))

    print("Total time:", time.perf_counter() - start_time)
    return len(loop_positions)

# Example usage for Part 2:
grid_example = [] ## read line for lines for wherever it is
# count_part2 = solve_part2(grid_example)
# print("Part 2 result:", count_part2)