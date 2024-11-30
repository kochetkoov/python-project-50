import pytest
from gendiff.scripts.gendiff import generate_diff

def test_generate_diff():
    assert generate_diff('file1.json', 'file2.json') == 'file1.json', 'file2.json'


