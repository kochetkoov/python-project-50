import argparse


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file',
                        type=str,
                        help='First configuration file')
    parser.add_argument('second_file',
                        type=str,
                        help='Second configuration file')
    parser.add_argument('-f', '--format',
                        type=str, help='Set format of output',
                        default='stylish')

    return parser.parse_args()
