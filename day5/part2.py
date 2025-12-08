from utils import readInput

def part2():
  (id_ranges, _) = readInput("./sampleInput")
  id_ranges = sorted(id_ranges, key=lambda x: int(x.split("-")[0]))
  id_count = get_all_numbers_in_range(id_ranges)
  assert id_count == 14
  (id_ranges, _) = readInput("./puzzleInput")
  id_count = get_all_numbers_in_range(id_ranges)
  print(id_count)

# 210542425538309 too low
# 452125362963180 too high
def get_all_numbers_in_range(id_ranges):
  # two scenarios:
  # the next range starts later than the previous but there is overlap
  #  the end may or may not be farther than before
  # the next range has no overlap. It starts higher than the previous end

  # in the first case, we just add the diff between the pointer and the end
  # in the second case, we just add the diff between the pointer and the start
  id_count = 0
  pointer = 0
  for id_range in id_ranges:
    start, end = id_range.split("-")
    if pointer < int(end):
      count_increase = (int(end) + 1) - max(int(start), pointer)
    pointer = max(pointer, int(end) + 1)
    print(f"increasing by {count_increase} from range {id_range} with pointer set at {pointer}")
    id_count += count_increase
  return id_count

if __name__ == "__main__":
  part2()
