from gendiff.gendiff import generate_diff
from gendiff.cli import parse_arguments


def main():
    args = parse_arguments()

    diff = generate_diff(args.first_file, args.second_file, args.format)

    print(diff)


if __name__ == "__main__":
    main()
