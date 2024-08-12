import os

""" The values on the initial seeds: line come in pairs. Within each pair, the
first value is the start of the range and the second value is the length of
the range. 
"""

"""
Dev notes
- 1st solution tried to create a list with all the seed numbers.
    With large input numbers that lead to running out of memory
- 2nd solution looped through each seed range by using for loop and range function
It takes a long time to calculate the final solution
- 3d solution. Need to optimize the brute force solution. Reddit thread suggested
    finding lowest value in each range.
    Why this could work? As we are looking for the lowest location value it
    would make sense that the smallest value in a range that is mapped also
    produces the lowest location number. Of course there are multiple conversions
    and a range might have to be split.

    https://www.reddit.com/r/adventofcode/comments/18buwiz/comment/kc6mtif/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    "So when you map the ranges, you end up with a list of ranges that contain
    all the results that you would have brute forced to check individually,
    so you just pick the range with the lowest starting positon, and then pick
    the first value in that range."
 """

def main():
    input_file = 'test1.txt'
    data_folder = 'data'
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    input_path = os.path.join(main_dir, data_folder, input_file)

    seed_ranges: list = []
    map_ranges: list = []
    temp_ranges: list = []

    with open(input_path, 'r') as file:
        for line in file:
            if 'seeds:' in line:
                seeds = [int(seed) for seed in line[6:].split()]
                for i, range_start in enumerate(seeds):
                    if i % 2 == 0:
                        seed_ranges.append([range_start, seeds[i + 1]])
                seeds.clear()
            if line == '\n' and temp_ranges:
                map_ranges.append(temp_ranges[:]) # copy list by value not ref
                temp_ranges.clear()
            elif line[0].isdigit():
                temp_ranges.append(string_list_to_int_list(line.split()))
    map_ranges.append(temp_ranges[:]) # copy list by value not ref
    temp_ranges.clear()
    
    print(f'Lowest location number: {mapper(seed_ranges, map_ranges)}')
            
def mapper(seed_ranges: list, map_ranges: list) -> int:
    lowest_location = -1

    for seed_range in seed_ranges:
        for seed in range(seed_range[0], seed_range[0] + seed_range[1]):
            for conversion in map_ranges:   
                for row in conversion:
                    if seed in range(row[1], row[1] + row[2]):
                        seed = seed + (row[0] - row[1])
                        break
            print(seed)
    #         if seed < lowest_location or lowest_location == -1:
    #             lowest_location = seed

    # return lowest_location

def string_list_to_int_list(data: list) -> list[int]:
    return [int(value) for value in data]


if __name__ == '__main__':
    main()

