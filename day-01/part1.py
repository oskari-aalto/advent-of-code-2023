import os

def main():
    filename = 'input.txt'
    data_folder = 'data'
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, data_folder)
    test_file = os.path.join(data_dir, filename)

    calibration_value: int = 0

    with open(test_file, 'r') as file:
        for line in file:
            line = line.strip()
            digits = []
            for c in line:
                if c.isdigit():
                    digits.append(c)
            calibration_value += int(f"{digits[0]}{digits[-1]}")
    print(calibration_value)

if __name__ == '__main__':
    main()