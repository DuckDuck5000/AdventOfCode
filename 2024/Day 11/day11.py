import sys
from functools import cache
from collections import Counter

grid = [line.strip() for line in sys.stdin if line.strip()]

def solve_25_blinks(map_data):
    stones = []
    for row in map_data:
        stones.extend(map(int, row.split()))
    
    for _ in range(25):
        new_stones = []
        for x in stones:
            x_str = str(x)
            if x == 0:
                new_stones.append(1)
            elif len(x_str) % 2 == 0:
                mid = len(x_str) // 2
                left_half = int(x_str[:mid])
                right_half = int(x_str[mid:])
                new_stones.append(left_half)
                new_stones.append(right_half)
            else:
                new_stones.append(x * 2024)
        stones = new_stones
    return len(stones)

def solve_75_blinks(map_data):
    stones = []
    for row in map_data:
        stones.extend(map(int, row.split()))
    
    @cache
    def f(x):
        if x == 0:
            return (1,)
        s = str(x)
        if len(s) % 2 == 0:
            mid = len(s) // 2
            return (int(s[:mid]), int(s[mid:]))
        else:
            return (x * 2024,)

    stone_count = Counter(stones)
    for _ in range(75):
        new_count = Counter()
        for val, cnt in stone_count.items():
            for transformed in f(val):
                new_count[transformed] += cnt
        stone_count = new_count
    
    return sum(stone_count.values())

print(solve_25_blinks(grid))
print(solve_75_blinks(grid))
