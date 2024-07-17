import os

def main():
    filename = 'input.txt'
    data_folder = 'data'
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_file = os.path.join(main_dir, data_folder)
    test_file = os.path.join(data_file, filename)


    with open(test_file, 'r') as file:
        for line in file:
            line = line.strip()
            digits = {}


if __name__ == '__main__':
    main()