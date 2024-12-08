
import Part1
import Part2

with open("input.txt", "r") as file:

  data = [list(row) for row in file.read().split()]

active = set()
for r, l in enumerate(data):
    for c, p in enumerate(l):
        if p == '#':
            active.add((r, c, 0))
print(active)

print(Part1.p1(active))

active = set()
for r, l in enumerate(data):
    for c, p in enumerate(l):
        if p == '#':
            active.add((r, c, 0, 0))


print(Part2.p2(active))


