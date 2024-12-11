import sys
from functools import cache
from collections import Counter

# Read lines from input, similar to the provided code snippet.
grid = [line.strip() for line in sys.stdin if line.strip()]

def solve_25_blinks(map_data):
    # map_data is a list of strings; each string may contain multiple numbers.
    # We'll parse all stones from all lines.
    stones = []
    for row in map_data:
        stones.extend(map(int, row.split()))
    
    # Perform 25 transformations (brute force)
    for _ in range(25):
        new_stones = []
        for x in stones:
            x_str = str(x)
            if x == 0:
                # Rule 1
                new_stones.append(1)
            elif len(x_str) % 2 == 0:
                # Rule 2
                mid = len(x_str) // 2
                left_half = int(x_str[:mid])
                right_half = int(x_str[mid:])
                new_stones.append(left_half)
                new_stones.append(right_half)
            else:
                # Rule 3
                new_stones.append(x * 2024)
        stones = new_stones
    return len(stones)

def solve_75_blinks(map_data):
    # Similar parsing for the second part.
    stones = []
    for row in map_data:
        stones.extend(map(int, row.split()))
    
    # Use a cached function and Counter-based approach for 75 transformations
    @cache
    def f(x):
        if x == 0:
            # Rule 1
            return (1,)
        s = str(x)
        if len(s) % 2 == 0:
            # Rule 2
            mid = len(s) // 2
            return (int(s[:mid]), int(s[mid:]))
        else:
            # Rule 3
            return (x * 2024,)

    stone_count = Counter(stones)
    for _ in range(75):
        new_count = Counter()
        for val, cnt in stone_count.items():
            for transformed in f(val):
                new_count[transformed] += cnt
        stone_count = new_count
    
    return sum(stone_count.values())

# Print results in similar style to the given code snippet
print(solve_25_blinks(grid))
print(solve_75_blinks(grid))
