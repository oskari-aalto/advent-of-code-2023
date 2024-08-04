import os

def main():
    input_file = 'input.txt'
    data_folder = 'data'
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    input_path = os.path.join(main_dir, data_folder, input_file)

    """ 
    You win copies of the scratchcards below the winning card equal to the
    number of matches. Process all of the original and copied scratchcards
    until no more scratchcards are won. Including the original set of
    scratchcards, how many total scratchcards do you end up with?
    """
    cards: dict = {}

    with open(input_path, 'r') as file:
        for line in enumerate(file):
            if not cards.get(line[0]):
                cards[line[0]] = 1
            else:
                cards[line[0]] += 1
            card = line[1].strip().split(': ')[1].split(' | ')
            copy_cards(line[0], cards, card_matching_numbers(card))
        file.close()
    print(sorted(cards.items()))
    print(f'FINAL SCORE: {sum(cards.values())}')

def card_matching_numbers(card: list) -> int:
    ''' Card list position 0 is winning numbers and position 0 player's numbers
    '''
    matching_numbers = 0
    for num in card[0].split():
        if num in card[1].split():
            matching_numbers += 1
    return matching_numbers

def copy_cards(card_num: int, cards: dict, matching_numbers: int):
    if matching_numbers > 0:
        for n in range(cards[card_num]):
            copies = matching_numbers
            while copies > 0:
                if card_num + copies not in cards:
                    cards[card_num + copies] = 1
                else:
                    cards[card_num + copies] += 1
                copies -= 1


if __name__ == '__main__':
    main()

