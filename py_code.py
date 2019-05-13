#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" file_lines.py - print the number of lines
        of python code in a directory. """
# import fileinput
import sys
from pathlib import Path
from typing import List

def file_len(file_name, encoding='utf8'):
    with open(file_name, encoding=encoding) as f:
        i = -1
        for i, line in enumerate(f):
            pass
    return i + 1

p = Path()
path = p.resolve()  # similar to os.path.abspath()
print(sum(file_len(f) for f in path.glob('*.py')))


"""
References:

original: https://towardsdatascience.com/bite-sized-python-recipes-52cde45f1489

"""
