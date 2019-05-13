#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" file_lines.py - calculate the number of lines in a file """
import fileinput
import sys
from pathlib import Path
from typing import List

# for line in fileinput.input(sys.argv[1:]):
#     mp3filename = line.strip()

def file_len(file_name, encoding='utf8'):
    with open(file_name, encoding=encoding) as f:
        i = -1
        for i, line in enumerate(f):
            pass
    return i + 1

p = Path()
path = p.resolve()  # similar to os.path.abspath()
print(sum(file_len(f) for f in path.glob('*.py')))


# print(file_len('file_lines.py', 'utf8'))


"""
References:

original: https://towardsdatascience.com/bite-sized-python-recipes-52cde45f1489

Calculate the Total Number of Lines in a File:

def file_len(file_name, encoding='utf8'):
    with open(file_name, encoding=encoding) as f:
        i = -1
        for i, line in enumerate(f):
            pass
    return i + 1

Example: How many lines of codes are there in the python files of your current directory?

>>> from pathlib import Path
>>> p = Path()
>>> path = p.resolve()  # similar to os.path.abspath()
>>> print(sum(file_len(f) for f in path.glob('*.py')))
745
"""
