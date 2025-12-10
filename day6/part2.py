def part2(file_path):
    matrix= []
    with open(file_path, 'r') as file: 
        for row, line in enumerate(file):
            matrix.append([])
            for element in line.split(' '):
                if len(element) > 0:
                  for character in element:
                      matrix[row].append(character)
                else:
                    matrix[row].append(element)
                
    # go through the last row and find the operator
    # work your way up the column to create the number
    # add it to the buffer
    # when we encounter a new operator, add the buffer to the solution

    
if __name__ == "__main__":
    part2('sampleInput')
