def read_input(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    return [list(line) for line in lines]

def part1(input_data):
    moving_lines = {}
    for i, ss in enumerate(input_data[0]):
        if ss == "S":
            moving_lines.append((0, i))
            break
    if len(moving_lines) == 0:
        ValueError("No starting point 'S' found in input data.")
    

def recursive_stuff(x, y, matrix, splits):
    '''
    Recursively see if something is being split
    '''
    pass



if __name__ == "__main__":
    input_data = read_input('sampleInput')
    print(part1(input_data))