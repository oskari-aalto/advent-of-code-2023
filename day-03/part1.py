import os

def main():
    input_file = 'input.txt'
    data_folder = 'data'
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    input_path = os.path.join(main_dir, data_folder, input_file)

    schematic: list = []
    answer = 0
    num = ''
    num_index = []

    with open(input_path, 'r') as file:
        for line in file:
            line = line.strip()
            schematic.append(line)
        file.close()

    """ Any number adjacent to a symbol, even diagonally, 
    is a "part number" and should be included in your sum 
    (Periods (.) do not count as a symbol.)
    """

    for row_num, row_data in enumerate(schematic):
        for char_index, char in enumerate(row_data):
            if not char.isdigit():
                if num:
                    # identified number > check if it is a part number
                    if check_part(schematic, row_num, num_index):
                        answer += int(num)
                    num = ''
                    num_index.clear()
            else:
                num += char
                num_index.append(char_index)
    
    print(answer)
    

def check_part(schematic: list, row_num: int, num_index: list) -> bool:
    # Check if part numbers are surrounded by "." or "empty"
    # Row -1, row and row +1
    # Unless first or last row
    row_helper = -1

    # Deal with row first and last char that have empty next to them
    if num_index[0] == 0:
        num_index.pop(0)
    elif num_index[-1] == len(schematic[row_num]):
        num_index.pop(-1)

    while row_helper < 2:
        if row_num == 0 and row_helper == -1:
            row_helper += 1
        elif row_num + row_helper == len(schematic):
            break
        else:
            for char in schematic[row_num + row_helper]\
                                 [num_index[0] - 1 : num_index[-1] + 2]:
                if char == '.' or char.isdigit():
                    continue
                else:
                    return True
            row_helper += 1
    return False
                

if __name__ == '__main__':
    main()

