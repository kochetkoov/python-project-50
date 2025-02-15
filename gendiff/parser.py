import json
import os

import yaml


def get_file_format(file_path):
    """ Get the data format from the file extension (e.., '.yaml"' -> 'yaml' """
    _, ext = os.path.splitext(file_path)
    return ext.lstrip('.').lower()


def parse_content(content, format):
    """ Parse file content based on its extension """
    if format == 'json':
        return json.loads(content)
    elif format in ['yml', 'yaml']:
        return yaml.safe_load(content)
    else:
        raise ValueError("Unsupported file format")


def read_file(file_path):
    """ Reads the content of a file and returns it as a string"""
    with open(file_path, 'r') as file:
        return file.read()


def load_data(file_path):
    """ Load and parse a file based on its extension """
    file_format = get_file_format(file_path)
    content = read_file(file_path)
    return parse_content(content, file_format)
