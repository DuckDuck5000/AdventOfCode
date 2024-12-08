with open('input.txt', 'r') as file:
  lines = file.readlines()
  lines = [line.rstrip() for line in lines]


SCORES = []
cost = 0
parenDict = {
  "(" : ")",
  "{" : "}",
  "[" : "]",
  "<" : ">"
}
costDic = {
  ")" : 3,
  "]" : 57,
  "}" : 1197,
  ">" : 25137
}

for line in lines:
  stack = []
  goodLine = True
  for let in line:
    if let in parenDict:
      stack.append(parenDict[let])
    elif let == stack[-1]:
      stack.pop()
    else:
      cost += costDic[let]
      break
      ## part 2
   if goodLine:
     score = 0
     P = {'(': 1, '[': 2, '{': 3, '<': 4}
     for c in range(len(S)-1, -1, -1):
         score = score*5 + P[S[c]]
     SCORES.append(score)
## Part 1
print(cost)
# Part 2
SCORES.sort()
print(SCORES[len(SCORES)//2])
