import os

def main():
    input_file = 'input.txt'
    data_folder = 'data'
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    input_path = os.path.join(main_dir, data_folder, input_file)

    total_points = 0

    """ 
    Calculate points for scratchcards
    each card has two lists of numbers separated by a vertical bar (|):
    a list of winning numbers and then a list of numbers you have.
    Figure out which of the numbers you have appear in the list of winning number
    The first match makes the card worth one point and
    each match after the first doubles the point value of that card.
    """

    with open(input_path, 'r') as file:
        for line in file:
            card = line.strip().split(': ')[1].split(' | ')
            total_points += calculate_points(card)
        file.close()
    print(f'POINTS: {total_points}')

def calculate_points(card: list) -> int:
    ''' Card list position 0 is winning numbers and position 0 player's numbers
    '''
    matching_numbers = 0
    for num in card[0].split():
        if num in card[1].split():
            matching_numbers += 1
    return 2 ** (matching_numbers - 1) if matching_numbers > 2 else matching_numbers


if __name__ == '__main__':
    main()

