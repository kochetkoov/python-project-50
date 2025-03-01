from pathlib import Path

import pytest

from gendiff.gendiff import generate_diff

FIXTURES_DIR = Path(__file__).parent / 'fixtures'

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
    file1_path = FIXTURES_DIR / file1
    file2_path = FIXTURES_DIR / file2
    expected = load_expected(expected_file)
    result = generate_diff(file1_path, file2_path, formatting)

    assert result == expected

@pytest.mark.parametrize(
    "file1, file2, format_name, expected_file",
    [
        ('non_existent_file.json', 'file3.json', 'stylish', 'result_generate_diff_stylish_2.txt'),
        ('file1.json', 'non_existent_file.json', 'plain', 'result_generate_diff_plain.txt'),
        ('file1.json', 'file2.json', 'invalid_format', 'result_invalid_format.txt')  # Некорректный формат
    ]
)


def test_generate_diff_invalid_inputs(file1, file2, format_name, expected_file):
    """Тестирование на некорректные входные данные (несуществующие файлы, неверный формат)"""
    file1_path = FIXTURES_DIR / file1
    file2_path = FIXTURES_DIR / file2

    if format_name == 'invalid_format':
        # Проверка на неправильный формат
        with pytest.raises(ValueError, match="Unknown format: invalid_format"):
            generate_diff(file1_path, file2_path, format_name)
    else:
        # Проверка на несуществующие файлы
        with pytest.raises(FileNotFoundError):
            generate_diff(file1_path, file2_path, format_name)


def load_expected(expected_file):
    expected_file_path = FIXTURES_DIR / expected_file
    with open(expected_file_path, 'r') as file:
        return file.read()