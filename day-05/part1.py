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
    temp_ranges: list = []

    with open(input_path, 'r') as file:
        for line in file:
            if 'seeds:' in line:
                seeds = [int(seed) for seed in line[6:].split()]
            if line == '\n' and temp_ranges:
                map_ranges.append(temp_ranges[:]) # copy list by value not ref
                temp_ranges.clear()
            elif line[0].isdigit():
                temp_ranges.append(string_list_to_int_list(line.split()))
    map_ranges.append(temp_ranges[:]) # copy list by value not ref
    temp_ranges.clear()
    
    mapper(seeds, map_ranges)
    print(f'Lowest location number: {min(seeds)}')
            
def mapper(seeds: list, map_ranges: list):
    for conversion in map_ranges:
        for pos, key in enumerate(seeds):
                for row in conversion:
                    if key in range(row[1], row[1] + row[2]):
                        seeds[pos] = key + (row[0] - row[1])
                        break
                else:
                    seeds[pos] = key
            
def string_list_to_int_list(data: list) -> list[int]:
    return [int(value) for value in data]


if __name__ == '__main__':
    main()

