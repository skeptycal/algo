#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" file_lines.py - calculate the number of lines in a file """
import json
# import fileinput
import sys
from pathlib import Path
from typing import Dict, List

BG_COLOR = "[48;5;230m"
HEADER = "[38;5;18m" + BG_COLOR
BLUE = "[38;5;27m" + BG_COLOR
PURPLE = "[38;5;92m" + BG_COLOR
RESET = "[0m"


def write_to_file(path: str, text: str) -> int:
    Path(path).write_text(text)
    return 0


def get_json(path: str) -> Dict:
    file = Path.cwd() / path
    try:
        with file.open() as data_file:
            result = json.load(data_file)
    except (FileNotFoundError, PermissionError) as e:
        print(e)
        result = {}
    return result


def file_len(file_name, encoding='utf8'):
    """ count number of lines in files """
    with open(file_name, encoding=encoding) as f:
        i = -1
        for i, line in enumerate(f):
            pass
    return i + 1


if __name__ == "__main__":
    walk_dir: str = ''
    if len(sys.argv) > 1:
        walk_dir = sys.argv[1]
    else:
        walk_dir = './'

    get_json('test.json')

    # print('walk_dir = ' + walk_dir)
    # print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
    # print('=> Directory Listing')
    # walk_it(walk_dir, True)

    # p = Path(walk_dir)
    # path = p.resolve()  # similar to os.path.abspath()
    # print(sum(file_len(f) for f in path.glob('**/*.py')))

    # print('for loop get contents: ("*.py")')
    # file_contents = [path.read_text() for path in Path.cwd().rglob('*.py')]
    # for lines in file_contents:
    #     print(lines)

# print(file_len('file_lines.py', 'utf8'))
"""
# [References](original: https://towardsdatascience.com/bite-sized-python-recipes-52cde45f1489)

"""
