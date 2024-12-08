part_1 = 0
vals = defaultdict(int)
for i,line in enumerate(lines):
  vals[i] += 1
  first, rest = line.split('|')
  id_, card = first.split(':')
  card_nums = [int(x) for x in card.split()]
  rest_nums = [int(x) for x in rest.split()]
  same_match = []
  for temp in set(card_nums):
    if temp in set(rest_nums): same_match.append(temp)
      
  if len(same_match) > 0:
    part_1 += 2**(len(same_match)-1)
  for j in range(len(same_match)):
    vals[i+1+j] += vals[i]
print(part_1)
print(sum(vals.values()))
