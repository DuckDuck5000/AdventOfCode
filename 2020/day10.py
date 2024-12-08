actualInput = rawInput.split("\n")

numbers = sorted([int(i) for i in actualInput])

import numpy as np
# problem 1
diffs = {}
a1 = np.array(numbers + [max(numbers) + 3])
a2 = np.array([0] + numbers)
unique, counts = np.unique(a1-a2, return_counts=True)
occ = dict(zip(unique, counts))
print(occ[1]*occ[3])

#problem 2
numbers = [0] + numbers + [max(numbers) + 3]
linkers = {n: 1 for n in numbers}
for i, n1 in enumerate(numbers):
    for j in (i+2, i+3):
        if j < len(numbers) and numbers[j] - n1 <= 3:
            for n2 in numbers[j:]:
                linkers[n2] += linkers[n1]
    

print(linkers[max(numbers)])
    
