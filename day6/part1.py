def part1(file_path):
  """
  Very quick and dirty solution that assumes a specific input format.
  
  :param file_path: Fun that it's modular by file path but doesn't 
  really work since you might have more or less numbers in your input file per problem
  """
  problems = []
  line_number = 1
  solution = 0
  with open(file_path, 'r') as file:
    for line in file:
       column_pointer = 0
       for element in line.split(' '):
          if element == '' or element == '\n':
             continue
          if line_number == 1:
             problems.append({"*": int(element), "+": int(element)})
          if line_number == 2 or line_number == 3 or line_number == 4:
              problems[column_pointer]["*"] *= int(element)
              problems[column_pointer]["+"] += int(element)
          if line_number == 5:
              if element == '*':
                  solution += problems[column_pointer]["*"]
              elif element == '+':
                  solution += problems[column_pointer]["+"]
          column_pointer += 1

       line_number += 1
  print(solution)


if __name__ == "__main__":
    part1('puzzleInput')