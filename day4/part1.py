from utils import readInput

def part1():
  sampleInput = readInput("./sampleInput")
  sampleResult = toilet_paper_hunting(sampleInput)
  assert sampleResult == 13
  puzzleInput = readInput("./puzzleInput")
  puzzleResult = toilet_paper_hunting(puzzleInput)
  print(puzzleResult)

def toilet_paper_hunting(matrix):
  accessible_rolls = 0
  for i, c in enumerate(matrix):
    for j, r in enumerate(c):
      touching_rolls = 0
      if r != '@':
        continue
      # check 8 adjacent cells

      # top left
      if i > 0 and j > 0 and matrix[i-1][j-1] == "@":
        touching_rolls += 1
      
      # top center
      if i > 0 and matrix[i-1][j] == "@":
        touching_rolls += 1

      # top right
      if i > 0 and j < len(c) - 1 and matrix[i-1][j+1] == "@":
        touching_rolls += 1

      # left
      if j > 0 and matrix[i][j-1] == "@":
        touching_rolls += 1

      # right
      if j < len(c) - 1 and matrix[i][j+1] == "@":
        touching_rolls += 1

      # bottom left
      if i < len(matrix) - 1 and j > 0 and matrix[i+1][j-1] == "@":
        touching_rolls += 1

      # bottom center
      if i < len(matrix) - 1 and matrix[i+1][j] == "@":
        touching_rolls += 1

      # bottom right
      if i < len(matrix) - 1 and j < len(c) - 1 and matrix[i+1][j+1] == "@":
        touching_rolls += 1

      if touching_rolls < 4:
        accessible_rolls += 1
  return accessible_rolls


if __name__ == "__main__":
  part1()
