import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    parser.add_argument('-f', '--format', help='set format of output')

    # парсим все аргументы
    args = parser.parse_args()

    with open(args.first_file, 'r') as file:
        first_data = json.load(file)

    with open(args.second_file, 'r') as file:
        second_data = json.load(file)

    # Пока что просто выводим аргументы для проверки
    print(f"Comparing '{args.first_file}' and '{args.second_file}'.")
    print(f'First file data: {first_data}')
    print(f'Second file data: {second_data}')


if __name__ == '__main__':
    main()

