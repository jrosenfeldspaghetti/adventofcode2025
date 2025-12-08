from utils import readInput

def part2():
  (id_ranges, _) = readInput("./sampleInput")
  id_ranges = sorted(id_ranges, key=lambda x: int(x.split("-")[0]))
  id_count = merge_ranges_and_get_all_numbers(id_ranges)
  print(id_count)
  assert id_count == 14
  (id_ranges, _) = readInput("./puzzleInput")
  id_ranges = sorted(id_ranges, key=lambda x: int(x.split("-")[0]))
  id_count = merge_ranges_and_get_all_numbers(id_ranges)
  print(id_count)

def merge_ranges_and_get_all_numbers(id_ranges):
  current_start = -1
  current_end = -1
  merged_ranges = []
  for id_range in id_ranges:
    start, end = id_range.split("-")
    start = int(start)
    end = int(end)
    if current_end == -1:
      current_start = start
      current_end = end
      continue
    if start <= current_end:
      if end > current_end:
        current_end = end
    else:
      # we've merged this range all we can
      merged_ranges.append((current_start, current_end))
      current_start = start
      current_end = end
  merged_ranges.append((current_start, current_end))
  return sum((end - start + 1) for (start, end) in merged_ranges)




if __name__ == "__main__":
  part2()
