array = rawInput.split("\n")

def numberOfTrees(array, directions):
    output = 1
    for direction in directions:
        count = 0
        currIndex = 0
        for line in range(0, len(array), direction[1]):
            if currIndex >= len(array[line]):
                currIndex -= len(array[line])
            if array[line][currIndex] == '#':
                count += 1
            currIndex += direction[0]
        output *= count
    return output

    
print(numberOfTrees(array,[(1,1), (3,1), (5, 1), (7, 1), (1, 2)]))
