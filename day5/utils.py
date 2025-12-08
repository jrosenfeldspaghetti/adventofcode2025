def readInput(filename):
  id_ranges = []
  in_ranges = True
  ids = []
  with open(filename) as f:
    for line in f:
      if line == "\n":
        in_ranges = False
        continue
      if in_ranges:
        id_ranges.append(line.strip())
      else:
        ids.append(line.strip())
  return (id_ranges, ids)
