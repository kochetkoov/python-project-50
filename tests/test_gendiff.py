from unittest.mock import patch

import pytest

from gendiff.gendiff import generate_diff


@pytest.fixture
def mock_generate_diff():
    with patch('gendiff.gendiff.format_plain') as mock_plain, patch('gendiff.gendiff.format_json') as mock_json:
        yield mock_plain, mock_json


def test_generate_diff_known_formats(mock_generate_diff):
    mock_plain, mock_json = mock_generate_diff

    # Мокаем возвращаемые значения для форматирования
    mock_plain.return_value = "Plain format result"
    mock_json.return_value = '{"json": "result"}'

    # Проверка для формата 'plain'
    result = generate_diff("file1.yaml", "file2.yaml", format_name='plain')
    assert result == "Plain format result"
    mock_plain.assert_called_once_with({'key': 'value'})  # Проверяем, что mock_plain был вызван с правильным аргументом

    # Проверка для формата 'json'
    result = generate_diff("file1.yaml", "file2.yaml", format_name='json')
    assert result == '{"json": "result"}'
    mock_json.assert_called_once_with({'key': 'value'})  # Проверяем, что mock_json был вызван с правильным аргументом


def test_generate_diff_invalid_format():
    # Тестируем для неизвестного формата, ожидаем выброс исключения
    with pytest.raises(ValueError, match="Unknown format: invalid_format"):
        generate_diff("file1.yaml", "file2.yaml", format_name='invalid_format')


def load_expected(file_name):
    with open(f'tests/fixtures/{file_name}', 'r') as file:
        return file.read().strip()


@pytest.mark.parametrize(
    "file1, file2, formatting, expected_file",
    [
        ('file3.json', 'file4.json',
         'stylish', 'result_generate_diff_stylish_2.txt'),
        ('file3.json', 'file3.json',
         'stylish', 'result_identical_files_stylish.txt'),
        ('empty.json', 'file3.json',
         'stylish', 'result_one_empty_file_stylish.txt'),
        ('empty.json', 'empty.json',
         'stylish', 'result_both_empty_files_stylish.txt'),
        ('file1.json', 'file2.json',
         'plain', 'result_generate_diff_plain.txt'),
        ('file4.json', 'file4.json',
         'plain', 'result_identical_files_plain.txt'),
        ('file1.json', 'empty.json',
         'plain', 'result_one_file_empty_plain.txt'),
        ('empty.json', 'empty.json',
         'plain', 'result_both_files_empty_plain.txt'),
        ('file1.json', 'file4.json',
         'json', 'result_different_files_json.txt'),
        ('empty.json', 'file4.json',
         'json', 'result_one_empty_file_json.txt'),
        ('file3.yml', 'file4.yml',
         'stylish', 'result_generate_diff_stylish_2.txt'),
        ('file3.yml', 'file3.yml',
         'stylish', 'result_identical_files_stylish.txt'),
        ('empty.yml', 'file3.yml',
         'stylish', 'result_one_empty_file_stylish.txt'),
        ('empty.yml', 'empty.yml',
         'stylish', 'result_both_empty_files_stylish.txt'),
        ('file1.yml', 'file2.yml',
         'plain', 'result_generate_diff_plain.txt'),
        ('file4.yml', 'file4.yml',
         'plain', 'result_identical_files_plain.txt'),
        ('file1.yml', 'empty.yml',
         'plain', 'result_one_file_empty_plain.txt'),
        ('empty.yml', 'empty.yml',
         'plain', 'result_both_files_empty_plain.txt'),
        ('file1.yml', 'file4.yml',
         'json', 'result_different_files_json.txt'),
        ('empty.yml', 'file4.yml',
         'json', 'result_one_empty_file_json.txt')
    ]
)


def test_generate_diff(file1, file2, formatting, expected_file):
    file1_path = f'tests/fixtures/{file1}'
    file2_path = f'tests/fixtures/{file2}'
    expected = load_expected(expected_file)
    assert generate_diff(file1_path, file2_path, formatting) == expected
