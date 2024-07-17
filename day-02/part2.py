import os

def main():
    input_file = 'input.txt'
    data_folder = 'data'
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    input_path = os.path.join(main_dir, data_folder, input_file)

    games = {}
    puzzle_input = 0

    with open(input_path, 'r') as file:
        for line in file:
            line = line.strip()
            game_round = line.split(': ')
            if game_round[1]:
                game_sets = game_round[1].split('; ')
            else:
                game_sets =  []
            games[int(game_round[0].strip('Game '))] = game_sets

    for id, game in games.items():
        print(id, game)
        bag = {'blue': 0,
               'green': 0,
               'red': 0}

        for round in game:
            round_cubes = round.split(', ')
            print(round_cubes)
            for cube in round_cubes:
                amount_color = cube.split()
                if bag.get(amount_color[1]) < int(amount_color[0]):
                    bag[amount_color[1]] = int(amount_color[0])
        prod = 1
        for n in bag.values():
            prod *= n
        puzzle_input += prod

    print(puzzle_input)

if __name__ == '__main__':
    main()

