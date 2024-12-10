import sys

grid = [line.strip() for line in ##input## if line.strip()]

def solve_topographic_map(map_data):
    g = [list(map(int, row)) for row in map_data]
    R, C = len(g), (len(g[0]) if g else 0)
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    memo = [[None]*C for _ in range(R)]

    def dfs(r, c):
        if memo[r][c] is not None:
            return memo[r][c]
        if g[r][c] == 9:
            memo[r][c] = {(r, c)}
            return memo[r][c]
        res = set()
        nh = g[r][c] + 1
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and g[nr][nc] == nh:
                res |= dfs(nr, nc)
        memo[r][c] = res
        return res

    ans = 0
    for r in range(R):
        for c in range(C):
            if g[r][c] == 0:
                ans += len(dfs(r, c))
    return ans

def solve_trailhead_ratings(map_data):
    g = [list(map(int, row)) for row in map_data]
    R, C = len(g), (len(g[0]) if g else 0)
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    memo = [[None]*C for _ in range(R)]

    def dfs(r, c):
        if memo[r][c] is not None:
            return memo[r][c]
        if g[r][c] == 9:
            memo[r][c] = 1
            return 1
        res = 0
        nh = g[r][c] + 1
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and g[nr][nc] == nh:
                res += dfs(nr, nc)
        memo[r][c] = res
        return res

    ans = 0
    for r in range(R):
        for c in range(C):
            if g[r][c] == 0:
                ans += dfs(r, c)
    return ans


print(solve_topographic_map(grid))
print(solve_trailhead_ratings(grid))
