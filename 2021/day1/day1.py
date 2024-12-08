with open('input.txt') as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

    
def day1(lines):
    count = 0
    count2 = 0
    for i in range(0, len(lines)):

    if i >=1 and lines[i] > lines[i-1]:
        count += 1
    if i >= 3:
        firstSum = lines[i-2] + lines[i-1] + lines[i-3]
        secondSum = lines[i] + lines[i-1] + lines[i-2]

        if secondSum > firstSum:
            count2 += 1
    return count, count2

print(day1(lines))

