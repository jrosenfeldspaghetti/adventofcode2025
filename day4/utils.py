def readInput(filename):
  rows = []
  with open(filename) as f:
    for line in f:
      rows.append(list(line))
  return rows