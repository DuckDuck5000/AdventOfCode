tempInput = rawInput.split('\n')

def twoSum(nums, target):
    
    h ={}
        
    for i, num in enumerate(nums):
        n = int(target) - int(num)
        if n not in h:
            h[int(num)] = i
        else:
            return None
    return False
    
def partOne(lines):
    
    for i in range(25, len(lines)):
        if twoSum(lines[i-25:i], lines[i]) == False:
            return lines[i]
    return None
    
def partTwo(lines):
    
    problemOne = int(partOne(lines))
    lines = [int(i) for i in lines]
    
    for i in range(len(lines)):
        for j in range(i+2, len(lines)):
            tempSum = lines[i:j]
            if sum(tempSum) == problemOne:
                tempSum.sort()
                return tempSum[0] + tempSum[-1]
    return None
        
    
print(partOne(tempInput))
print(partTwo(tempInput))
