import os

"""
seed_to_soil
soil_to_fertilizer
fertilizer_to_water
water_to_light
light_to_temperature
temperature_to_humidity
humidity_to_location

destination <<< source --- range length
soil <<< seed
fertilizer <<< soil
"""

def main():
    input_file = 'input.txt'
    data_folder = 'data'
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    input_path = os.path.join(main_dir, data_folder, input_file)

    seeds: list = []
    map_ranges: list = []
    key_map: int = -1

    with open(input_path, 'r') as file:
        for line in file:
            if 'seeds:' in line:
                # seeds = dict([(int(key), [-1 for _ in range(num_of_maps)]) 
                #                 for key in line[6:].split()])
                seeds = [int(seed) for seed in line[6:].split()]
                print(f'{seeds} : initial seeds')

            if line == '\n':
                if map_ranges:
                    mapper(seeds, map_ranges)
                    print(f'{seeds} : {key_map}')
                    map_ranges.clear()
                key_map += 1

            elif key_map == 0 and line[0].isdigit():
                map_ranges.append(string_list_to_int_list(line.split()))
            elif key_map == 1 and line[0].isdigit():
                map_ranges.append(string_list_to_int_list(line.split()))
            elif key_map == 2 and line[0].isdigit():
                map_ranges.append(string_list_to_int_list(line.split()))
            elif key_map == 3 and line[0].isdigit():
                map_ranges.append(string_list_to_int_list(line.split()))
            elif key_map == 4 and line[0].isdigit():
                map_ranges.append(string_list_to_int_list(line.split()))
            elif key_map == 5 and line[0].isdigit():
                map_ranges.append(string_list_to_int_list(line.split()))
            elif key_map == 6 and line[0].isdigit():
                map_ranges.append(string_list_to_int_list(line.split()))
            elif key_map == 7 and line[0].isdigit():
                map_ranges.append(string_list_to_int_list(line.split()))
    
    mapper(seeds, map_ranges)
    print(f'{seeds} : {key_map}')
    print(f'Lowest location number: {min(seeds)}')

            
def mapper(seeds: list, map_ranges: list):
    for pos, key in enumerate(seeds):
        for row in map_ranges:
            if key in range(row[1], row[1] + row[2]):
                seeds[pos] = key + (row[0] - row[1])
                break
        else:
            seeds[pos] = key
            
def string_list_to_int_list(data: list) -> list[int]:
    return [int(value) for value in data]


if __name__ == '__main__':
    main()

