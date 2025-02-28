import pytest
from gendiff.formatters.stylish import (
    format_value,
    handle_unchanged,
    handle_added,
    handle_removed,
    handle_updated,
    handle_nested,
    format_stylish
)


def test_format_value():
    # Проверка для различных типов значений
    assert format_value(True) == 'true'
    assert format_value(False) == 'false'
    assert format_value(None) == 'null'
    assert format_value(42) == '42'
    assert format_value('string') == 'string'
    assert format_value({'key': 'value'}) == "{\n        key: value\n    }"  # Пример для словаря
