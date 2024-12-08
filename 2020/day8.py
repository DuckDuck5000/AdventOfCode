def partOne(array):
    
    visited = []
    rollingSum = 0
    index = 0
    
    while True:
        if index > len(array):
            return rollingSum
        move, distance = array[index].split(' ')[0], int(array[index].split(' ')[1])
        
        if index in visited:
            return rollingSum
        visited.append(index)
        if move == 'nop':
            index += 1
        elif move == 'acc':
            rollingSum += distance
            index += 1
        elif move == 'jmp':
            index += distance
 
 
output = rawInput.split('\n')
lines = []
for line in output:
    line = line.rstrip().split(' ')
    lines.append([line[0], int(line[1])])
def move(lines, part_1=False):
    seen = set()
    accumulator = 0
    idx = 0
    while True:
        if idx >= len(lines):
            return accumulator
        move, arg = lines[idx]
        if idx in seen:
            return accumulator if part_1 else False
        seen.add(idx)
        if move == 'nop':
            idx += 1
        elif move == 'acc':
            accumulator += arg
            idx += 1
        elif move == "jmp":
            idx += arg


def flip(val):
    return 'jmp' if val == 'nop' else 'nop'


def change_piece(lines):
    for idx, turn in enumerate(lines):
        if turn[0] == 'nop' or turn[0] == 'jmp':
            prev = turn[0]
            lines[idx][0] = flip(turn[0])
            if accumulator:= move(lines):
                return accumulator
            lines[idx][0] = prev

