import argparse
import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1:
        data1 = json.load(file1)

    with open(file_path2, 'r') as file2:
        data2 = json.load(file2)

    keys = sorted(set(data1.keys()).union(data2.keys()))
    diff = []

    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f"    {key}: {data1[key]}")
            else:
                diff.append(f"  - {key}: {data1[key]}")
                diff.append(f"  + {key}: {data2[key]}")
        elif key in data1:
            diff.append(f"  - {key}: {data1[key]}")
        elif key in data2:
            diff.append(f"  + {key}: {data2[key]}")

    return "{\n" + "\n".join(diff) + "\n}"


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    parser.add_argument('-f', '--format', help='set format of output')

    # парсим все аргументы
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file)
    print(result)


if __name__ == '__main__':
    main()