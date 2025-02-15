### Hexlet tests and linter status:
[![Actions Status](https://github.com/kochetkoov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/kochetkoov/python-project-50/actions/hexlet-check.yml) 
[![Maintainability](https://api.codeclimate.com/v1/badges/40413e95b9fc7998f651/maintainability)](https://codeclimate.com/github/kochetkoov/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/40413e95b9fc7998f651/test_coverage)](https://codeclimate.com/github/kochetkoov/python-project-50/test_coverage)

## The Gendiff Project

### This project was made to help to find out the difference between two files and make this process easier and faster, enjoy!

## How to show help message:
Use CLI and type this command: 
``` sh
gendiff -h
```
 ![asciicast](https://asciinema.org/a/yqm2SFser6KZmcvhUHNfSh9Jf.svg)

## To compare two files (JSON or YAML) use this command:
``` sh
gendiff filepath1.json filepath2.json
gendiff filepath1.yml filepath2.yml
```

## To use build in formatters use this command:
``` sh
-f/--format - the flag which allows to choose any formatter
Stylish format is used by default
gendiff -f stylish filepath1 filepath2 - to show stylish ouput
gendiff -f plain filepath1 filepath2 - to show plain output
gendiff -f json filepath1 filepath2 - to show json output
```

## Here's the example of 'stylish' comparing JSON and YAML files:
 ![asciicast](https://asciinema.org/a/H6xU2wSSLv08NDAtmkrkEWUXj.svg)

## Here's the example of 'plain' comparing JSON and YAML files:
 ![asciicast](https://asciinema.org/a/3Q0Q5SQGdzIsS7vCrIlb0qRzo.svg)

## Here's the example of formattind diff into JSON format:
![asciicast](https://asciinema.org/a/kpQfZ2qY5gIzE9n7ELjlmnWvs.svg)

### Installation requirements and instruction.
Installation requirements:
1. CPython
2. Poetry
3. Git
4. Make

How to install the project:
1. Clone this project repo(git clone "url of the project").
2. Cd to the cloned project.
3. Use command "make build" to build the package.
4. Install the build package using pip.
5. Use the project.

## Important note:

## If you want to check the project's code you always can use "make lint" command to use a linter built in a project.

### Links

| Tool                                 | Description |
|--------------------------------------|-------------|
| [poetry](https://python-poetry.org/) | "Python dependency management and packaging made easy" |
| [flake8](https://flake8.pycqa.org/en/latest/) | "Your tool for style guide enforcement" |
