tempOutput = rawInput.split("\n\n")

from collections import Counter
def partOne(array):
    
    counter = 0
    
    for group in array:
        for key, value in Counter(group).items():
            if key != '\n':
                counter += 1
    return counter

def partTwo(array):
    
    counter = 0
    
    for group in array:
        temp = Counter(group)
        for key, value in temp.items():
            if key != '\n' and value == temp['\n']+1:
                counter += 1
    return counter
