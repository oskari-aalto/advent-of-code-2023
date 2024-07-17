import os

def main():
    filename = 'test-1.txt'
    data_folder = 'data'
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_file = os.path.join(main_dir, data_folder)
    filepath = os.path.join(data_file, filename)

    bag = {'blue': 14,
           'green': 13,
           'red': 12}

    games = {}
    with open(filepath, 'r') as file:
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
        for round in game:
            round_cubes = round.split(', ')
            print(round_cubes)
            for j in round_cubes:
                amount_color = j.split()
                if bag.get(amount_color[1]) < int(amount_color[0]):
                    print(f'impossible: {amount_color}')
                    break
            else:
                continue
            break
        print(id)

if __name__ == '__main__':
    main()

