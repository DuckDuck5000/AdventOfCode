import time
class Read:

  def createGraph(self):
    graph = {}
    for line in  open('input.txt', 'r'):
      start, end = line.strip().split('-')

      if start not in graph:
        graph[start] = [end]
      else:
        graph[start].append(end)
      if end not in graph:
        graph[end] = [start]
      else:
        graph[end].append(start)
    return graph

class Solution:

  def __init__(self, data):
    self.graph = data

  def solver(self, isPartTwo=True):
      start = ('start', set(['start']), None)
      q = [start]
      totalPaths = 0
      while q:
        position, set1, rep = q.pop(0)
        if position == 'end':
          totalPaths += 1
          continue
      
        for pos in self.graph[position]:
          if pos not in set1:
            new_set = set(set1)

            if pos.lower() == pos:
              new_set.add(pos)
            q.append((pos, new_set, rep))
            ## Part Two add on
          elif isPartTwo:
            if pos in set1 and pos not in ['start', 'end'] and rep is None:
              q.append((pos, set1, pos))
      return totalPaths


if __name__ == "__main__":
  start = time.perf_counter()
  data = Read().createGraph()

  Solutions = Solution(data)

  print("Part One ", Solutions.solver(False))
  print("Part Two ", Solutions.solver())
  end = time.perf_counter()
  print("Total time", end-start)
