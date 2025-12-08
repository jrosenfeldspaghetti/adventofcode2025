from utils import readInput, adjacent_count

def part2():
  sampleInput = readInput("./sampleInput")
  sampleResult = advanced_paper_hunting(sampleInput)
  assert sampleResult == 43
  puzzleInput = readInput("./puzzleInput")
  puzzleResult = advanced_paper_hunting(puzzleInput)
  print(puzzleResult)


def advanced_paper_hunting(matrix):
  accessible_rolls = 0
  previous_rolls = -1
  while accessible_rolls != previous_rolls:
    previous_rolls = accessible_rolls
    for i, c in enumerate(matrix):
      for j, r in enumerate(c):
        touching_rolls = 0
        if r != '@':
          continue
        # check 8 adjacent cells
        touching_rolls = adjacent_count(matrix, i, j)
        if touching_rolls < 4:
          accessible_rolls += 1
          matrix[i][j] = '.'

  return accessible_rolls

if __name__ == "__main__":
  part2()