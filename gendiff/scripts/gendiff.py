import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    # Пока что просто выводим аргументы для проверки
    print(f"Comparing '{args.first_file}' and '{args.second_file}'.")


if __name__ == '__main__':
    main()
