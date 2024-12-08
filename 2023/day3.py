import re
from collections import defaultdict

# Read lines from the file
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

# Compile regex pattern for numbers
num_pattern = re.compile(r'\d+')

# Process each line
gear = defaultdict(list)
part1 = 0
for i, line in enumerate(lines):
    for match in re.finditer(num_pattern, line):
        all_good = any(
            0 <= y < len(lines) and 0 <= x < len(lines[y]) and lines[y][x] == '*'
            for y in range(i-1, i+2)
            for x in range(match.start()-1, match.end()+1)
        )

        if all_good:
            part1 += int(match.group())
            gear[(i, match.start())].append(int(match.group()))

print(part1)

# Calculate part 2
part2 = sum(v[0] * v[1] for v in gear.values() if len(v) == 2)
print(part2)
