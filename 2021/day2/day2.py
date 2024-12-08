with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def part1(lines):

  horz, vert = 0, 0

  for line in lines:
    direction, delta = line.split()[0], int(line.split()[1])

    if direction == "forward":
      horz += delta
    elif direction == "up":
      vert -= delta
    else:
      vert += delta

  return horz*vert

def part2(lines): 

  aim, horz, vert = 0, 0, 0

  for line in lines:
      direction, delta = line.split()[0], int(line.split()[1])

      if direction == "forward":
        horz += delta
        vert += (delta*aim)
      elif direction == "up":
        aim -= delta
      else:
        aim += delta
  return horz*vert

print(part1(lines))
print(part2(lines))
