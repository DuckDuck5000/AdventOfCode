
'''
from collections import defaultdict

with open('input.txt', 'r') as file:
  lines = file.readlines()
  lines = [(line.rstrip()) for line in lines]

finalCount = 0
for line in lines:
  if '|'  not in line:
    pass
  else:
    start, line = line.split('|')
    #line = end.split(',')
    line = line.split(' ')

    

    for word in line:
      tempDic = {}
      count = 0
      for letter in word:
        if letter not in tempDic:
          tempDic[letter] = 1
          count += 1
      if count in [2, 4, 3, 7]:
        finalCount += 1
print(finalCount)



# initialize dict

numDict = defaultdict(list)
sumDic = {}

sumDic[4] = [4]
sumDic[2] = [1]
sumDic[6] = [0, 6, 9]
sumDic[3] = [7]
sumDic[5] = [5, 3, 2]
sumDic[7] = [8]

finalSum = 0
for line in lines:
  if '|'  not in line:
    pass
  else:
    start, line = line.split('|')
    #line = end.split(',')
    line = line.split()
    start = start.split()
    numDic = {}
    for word in start:

      trans = ''.join(sorted(list(word)))

      numDict[len(trans)].append(trans)

    print(line)
    tempSum = ""
    for word in line:
      if word == "":
        pass
      else:
        trans2 = ''.join(sorted(list(word)))

        for i in range(0, len(numDict[len(trans2)])):
          if trans2 == numDict[len(trans2)][i]:
            print(trans2)
            print(i)
            print(numDict)
            tempSum += str(sumDic[len(trans2)][i])
    finalSum += int(tempSum)
print(finalSum)
'''
import itertools
from collections import defaultdict, Counter

# 0: abcefg (6)
# 6: abdefg (6)
# 9: abcdfg (6)

# 2: acdeg (5)
# 3: acdfg (5)
# 5: abdfg (5)

# 1: cf (2)
# 4: bcdf (4)
# 7: acf (3)
# 8: abcdefg (7)

digits = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}


def find_perm(before):
    A = {}
    for w in before:
        if len(w) == 2: # 1
            cf = w
    assert len(cf) == 2, cf
    for w in before:
        if len(w) == 6 and (cf[0] in w)!=(cf[1] in w): # 6
            if cf[0] in w:
                A[cf[0]] = 'f'
                A[cf[1]] = 'c'
            else:
                A[cf[1]] = 'f'
                A[cf[0]] = 'c'
    assert len(A) == 2, f'A={A} cf={cf} {before}'
    for w in before:
        if len(w)==3: # 7
            for c in w:
                if c not in cf:
                    A[c] = 'a'
    assert len(A) == 3, A
    for w in before:
        if len(w)==4: #4
            bd = ''
            for c in w:
                if c not in cf:
                    bd += c
    assert len(bd) == 2, bd
    # 0 is length-6 and missing one of b/d. B is present; D is missing.
    # 9 is length-6 missing one of e/g. G is present; E is missing.
    for w in before:
        if len(w)==6 and (bd[0] in w)!=(bd[1] in w): # 0
            if bd[0] in w:
                A[bd[0]] = 'b'
                A[bd[1]] = 'd'
            else:
                A[bd[1]] = 'b'
                A[bd[0]] = 'd'
    assert len(A) == 5, A
    eg = ''
    for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
        if c not in A:
            eg += c
    assert len(eg) == 2, eg
    for w in before:
        if len(w) == 6 and (eg[0] in w)!=(eg[1] in w): # 9
            if eg[0] in w:
                A[eg[0]] = 'g'
                A[eg[1]] = 'e'
            else:
                A[eg[1]] = 'g'
                A[eg[0]] = 'e'
    assert len(A) == 7, A
    return A

p1 = 0
ans = 0

with open('input.txt', 'r') as file:
  lines = file.readlines()
  lines = [(line.rstrip()) for line in lines]
for line in lines:
    before, after = line.split('|')
    before = before.split()
    after = after.split()


    D = find_perm(before)
    ret = ''
    for w in after:
        w_perm = ''
        for c in w:
            w_perm += D[c]
        w_perm = ''.join(sorted(w_perm))
        d = [k for k,v in digits.items() if v==w_perm]
        assert len(d)==1
        if d[0] in [1,4,7,8]:
            p1 += 1
        ret += str(d[0])
    ans += int(ret)
print(p1)
print(ans)




