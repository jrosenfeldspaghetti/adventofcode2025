from utils import readInput

def part1():
  (id_ranges, ids) = readInput("./sampleInput")
  valid_ids = calculate_number_of_valid_ids(id_ranges, ids)
  assert valid_ids == 3
  (id_ranges, ids) = readInput("./puzzleInput")
  valid_ids = calculate_number_of_valid_ids(id_ranges, ids)
  print(valid_ids)


def calculate_number_of_valid_ids(id_ranges, ids):
  valid_ingredients = 0
  for ingredient in ids:
    for id_range in id_ranges:
      start, end = id_range.split("-")
      if int(ingredient) >= int(start) and int(ingredient) <= int(end):
        valid_ingredients += 1
        break
  return valid_ingredients

if __name__ == "__main__":
  part1()
