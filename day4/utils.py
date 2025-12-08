def readInput(filename):
  rows = []
  with open(filename) as f:
    for line in f:
      rows.append(list(line))
  return rows

def adjacent_count(matrix, i, j):
  touching_rolls = 0

  # top left
  if i > 0 and j > 0 and matrix[i-1][j-1] == "@":
    touching_rolls += 1
  
  # top center
  if i > 0 and matrix[i-1][j] == "@":
    touching_rolls += 1

  # top right
  if i > 0 and j < len(matrix[i]) - 1 and matrix[i-1][j+1] == "@":
    touching_rolls += 1

  # left
  if j > 0 and matrix[i][j-1] == "@":
    touching_rolls += 1

  # right
  if j < len(matrix[i]) - 1 and matrix[i][j+1] == "@":
    touching_rolls += 1

  # bottom left
  if i < len(matrix) - 1 and j > 0 and matrix[i+1][j-1] == "@":
    touching_rolls += 1

  # bottom center
  if i < len(matrix) - 1 and matrix[i+1][j] == "@":
    touching_rolls += 1

  # bottom right
  if i < len(matrix) - 1 and j < len(matrix[i]) - 1 and matrix[i+1][j+1] == "@":
    touching_rolls += 1
  return touching_rolls