from unittest import mock

from gendiff.scripts.cli import parse_arguments


# Тест, проверяющий правильность парсинга аргументов
def test_parse_arguments_valid():
    # Мокируем аргументы командной строки
    mock_args = ['gendiff', 'file1.json', 'file2.json', '-f', 'plain']
    with mock.patch('sys.argv', mock_args):
        args = parse_arguments()

    # Проверяем, что аргументы корректно парсятся
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'plain'


# Тест, проверяющий, что по умолчанию формат output будет 'stylish'
def test_parse_arguments_default_format():
    # Мокируем аргументы командной строки
    mock_args = ['gendiff', 'file1.json', 'file2.json']
    with mock.patch('sys.argv', mock_args):
        args = parse_arguments()

    # Проверяем, что формат вывода по умолчанию 'stylish'
    assert args.format == 'stylish'

