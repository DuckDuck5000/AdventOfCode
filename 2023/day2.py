import collections

def parse_line(line):
    values = collections.defaultdict(int)
    for event in line.split(';'):
        for balls in event.split(','):
            n, color = balls.split()
            n = int(n)
            values[color] = max(values[color], n)
    return values

COLOR_LIMITS = {'red': 12, 'green': 13, 'blue': 14}

# Part 1
p1 = 0
for line in lines:
    id_, line_content = line.split(':')
    values = parse_line(line_content)
    if all(n <= COLOR_LIMITS.get(color, 0) for color, n in values.items()):
        p1 += int(id_.split()[-1])
print(p1)

# Part 2
p2 = 0
for line in lines:
    _, line_content = line.split(':')
    values = parse_line(line_content)
    score = 1
    for v in values.values():
        score *= v
    p2 += score
print(p2)
