from utils import readInput, adjacent_count

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
      touching_rolls = adjacent_count(matrix, i, j)
      if touching_rolls < 4:
        accessible_rolls += 1
  return accessible_rolls


if __name__ == "__main__":
  part1()
