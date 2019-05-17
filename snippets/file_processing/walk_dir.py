#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" walk_dir.py """
# pylint: disable=redefined-outer-name,missing-docstring
import os
import random
from math import log10, ceil
import sys
from functools import wraps
from pathlib import Path
from time import time
from typing import List, Tuple, Sequence

BG_COLOR = "[48;5;230m"
HEADER = "[38;5;18m" + BG_COLOR
BLUE = "[38;5;27m" + BG_COLOR
PURPLE = "[38;5;92m"
RESET = "[0m"

HUMAN_READABLE: Tuple = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')

TIMER_FORMAT_LONG: str = "=> The function " + HEADER + "{0:<10s}" + RESET + " executed in " + HEADER + "{1:>10.4f}" + RESET + " seconds."

REPORT_FORMAT: str = "Time for " + HEADER + "{:<.30}" + RESET + "was {:>5.3f} s."

SCRIPT_NAME: str = sys.argv[0]


def timeit(func):
    """
    :param func: Decorated function
    :return: Execution time for the decorated function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(REPORT_FORMAT.format(func.__name__, end - start))
        return result

    return wrapper


def human_readable(n: int) -> str:
    """ Return string with integer converted to 'human readable' format
            log10 is 400% faster than str / int conversions and
            somewhat faster than cascasding if statements with division."""
    l = ceil(log10(n)) - 1
    if l > 8:
        l = 8
    return str(round(n / (1.024 * 10**l)), 2) + ' ' + HUMAN_READABLE[l]


def walk_it(walk_dir: str = '.', recursive: bool = True,
            dirfirst: bool = True) -> Sequence[Path]:
    """ print directory listing with recursive option """
    result: Sequence = []
    p: Path = Path(walk_dir).resolve()
    d: Path = p.parents[0]
    print('=> Starting walk_it path tests: ', HEADER, SCRIPT_NAME, RESET, '\n')
    print('  - diagnostics:')
    print("\t\t- p absolute: ", p)
    print("\t\t- d - p.parents[0] ", d)
    print("\t\t- p.exists: ", p.exists())
    print("\t\t- d exists: ", d.exists())
    if not d.is_dir():
        return []
    if not recursive:
        # print('p.glob ', list(d.glob('*')))
        result = d.glob('*')
    else:
        # print('d.rglob ', list(d.rglob('*')))
        result = d.rglob('*')
    if dirfirst:
        result.sorted()
    return result

class tprint(print):
    def __repr__(self):
        return super().__repr__()
    pass


def main(test: bool = False):
    walk_dir: str = ''
    dir_first: bool = True
    color: str = RESET

    if len(sys.argv) > 1:
        walk_dir = sys.argv[1]
    else:
        walk_dir = '*.py'

    tprint("nn")
    tprint('=> Directory Listing\n')

    dir_list: Sequence[Path] = walk_it(walk_dir, True)
    if dir_first:
        color = BLUE
        dirs = '\n'.join([f.parts[-1] for f in dir_list if f.is_dir()])
        print(color, dirs)
        color = RESET
        files = '\n'.join([f.parts[-1] for f in dir_list if not f.is_dir()])
        print(color, files)
    else:
        for f in dir_list:
            if f.is_dir():
                color = BLUE
                print(color, '/'.join(f.parts[-2:]), RESET)
                lastdir = f
            else:
                color = RESET
                print(color, f.parts[-1], RESET)


if __name__ == "__main__":
    main()
