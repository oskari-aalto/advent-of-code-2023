import os

def main():
    input_file = 'input.txt'
    data_folder = 'data'
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    input_path = os.path.join(main_dir, data_folder, input_file)

    schematic: list = []
    answer: int = 0

    with open(input_path, 'r') as file:
        for line in file:
            line = line.strip()
            schematic.append(line)
        file.close()

    """ A gear is any * symbol that is adjacent to exactly two part numbers.
    Its gear ratio is the result of multiplying those two numbers together.
    Find the gear ratio of every gear and add them all.
    """

    for row_num, row_data in enumerate(schematic):
        for char_index, char in enumerate(row_data):
            if char == '*':
                answer += check_gear(schematic, row_num, char_index)
            else:
                continue

    print(answer) # Correct: 79026871

def check_gear(schematic: list, row_num: int, gear_index: int) -> int:
    # Find numbers in adjacent rows and current row
    # Check if found number is next to gear
    # If more than 2 numbers not a gear
    # Return gear ratio

    num: str = ''
    num_index: list = []
    row_helper = -1
    gear_ratio = 1
    num_count = 0

    while row_helper < 2:
        if row_num == 0 and row_helper == -1:
            row_helper += 1
        elif row_num + row_helper == len(schematic):
            break
        else:
            # Find all numbers and their indices in selected rows
            for char_index, char in enumerate(schematic[row_num + row_helper]):
                if not char.isdigit():
                    if num:
                        for i in num_index:
                            if gear_index - 1 <= i <= gear_index + 1:
                                gear_ratio *= int(num)
                                num_count += 1
                                break
                        num = ''
                        num_index.clear()
                else:
                    num += char
                    num_index.append(char_index)
            row_helper += 1
    
    if num_count == 2:
        return gear_ratio
    else:
        return 0

if __name__ == '__main__':
    main()

