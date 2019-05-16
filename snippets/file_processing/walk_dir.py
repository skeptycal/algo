#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" walk_dir.py """
# pylint: disable=redefined-outer-name,missing-docstring
import os
import random
import sys
from functools import wraps
from pathlib import Path
from time import time
from typing import List

BG_COLOR = "[48;5;230m"
HEADER = "[38;5;18m" + BG_COLOR
BLUE = "[38;5;27m" + BG_COLOR
PURPLE = "[38;5;92m" + BG_COLOR
RESET = "[0m"

# TIMER_FORMAT = "=> The function " + BLUE + "{0:<10s}" + RESET + " executed in " + PURPLE + "{1:>10.4f}" + RESET + " seconds."

# def timeit(func):
# """
# :param func: Decorated function
# :return: Execution time for the decorated function
# """

# @wraps(func)
# def wrapper(*args, **kwargs):
#     start = time()
#     result = func(*args, **kwargs)
#     end = time()
#     print(TIMER_FORMAT.format(func.__name__, end - start))
#     return result

# return wrapper


# @timeit
def h_num1(n: int) -> str:
    """ convert integer to 'human readable' formatted string """
    # i: float = 0
    # i = round(n / 1000)
    # for i in range(0, 25, 3):
    #     if n > 1.024 * 10 ** i:
    if n >= 1024000000000000000000000:
        return str(round(n / (1.024 * 10**24), 1)) + ' YB'
    if n >= 1024000000000000000000:
        return str(round(n / (1.024 * 10**21), 1)) + ' ZB'
    if n >= 1024000000000000000:
        return str(round(n / (1.024 * 10**18), 1)) + ' EB'
    if n >= 1024000000000000:
        return str(round(n / (1.024 * 10**15), 1)) + ' PB'
    if n >= 1024000000000:
        return str(round(n / (1.024 * 10**12), 1)) + ' TB'
    if n >= 1024000000:
        return str(round(n / (1.024 * 10**9), 1)) + ' GB'
    if n >= 1024000:
        return str(round(n / (1.024 * 10**6), 1)) + ' MB'
    if n >= 1024:
        return str(round(n / (1.024 * 10**3), 1)) + ' KB'
    return str(round(n, 1)) + ' B'


# @timeit
def h_num(n: int) -> str:
    """ convert integer to 'human readable' formatted string """
    # i: float = 0
    # i = round(n / 1000)
    # for i in range(0, 25, 3):
    #     if n > 1.024 * 10 ** i:
    for i in range(1000000):
        if n <= 1024:
            return str(round(n, 1)) + ' B'
        if n <= 1024000:
            return str(round(n / (1.024 * 10**3), 1)) + ' KB'
        if n <= 1024000000:
            return str(round(n / (1.024 * 10**6), 1)) + ' MB'
        if n <= 1024000000000:
            return str(round(n / (1.024 * 10**9), 1)) + ' GB'
        if n <= 1024000000000000:
            return str(round(n / (1.024 * 10**12), 1)) + ' TB'
        if n <= 1024000000000000000:
            return str(round(n / (1.024 * 10**15), 1)) + ' PB'
        if n <= 1024000000000000000000:
            return str(round(n / (1.024 * 10**18), 1)) + ' EB'
        if n <= 1024000000000000000000000:
            return str(round(n / (1.024 * 10**21), 1)) + ' ZB'
        if n <= 1024000000000000000000000000:
            return str(round(n / (1.024 * 10**24), 1)) + ' YB'


def repeat_func():
    for j in range(100000):
        X = h_num()


def walk_it(walk_dir: str = '*/*', recursive: bool = True) -> List[str]:
    """ print directory listing with recursive option """
    result = []
    p = Path(walk_dir).absolute()
    d = p.parents[0]
    print(HEADER, 'walk_it path tests: ', sys.argv[0], RESET)
    print("p absolute: ", p)
    print("p.exists: ", p.exists())
    print("d parents: ", d)
    print('d exists', d.exists())
    if not d.exists():
        p = Path.cwd() / '*.*'
    dir_list = [x.as_posix() for x in d.iterdir() if x.is_dir()]
    print(list(p.glob('*')))
    result = dir_list
    # print('\n'.join(dir_list))
    # print(TIMER_FORMAT)

    return result
    # last_path: str = ''
    # result: List = []
    # try:
    #     walk_dir = Path(walk_dir).resolve()
    # except FileNotFoundError:
    #     walk_dir = Path.cwd() / "*.*"
    # file_list = Path(walk_dir).rglob(walk_dir) if recursive else Path(
    #     walk_dir).glob(walk_dir)

    # for file in file_list:  # use rglob for recursive
    #     print(Path.stat(file))
    # return result


# def tests(n: int, v: int) -> int:
#     """ test number formats
#             n: int  -  number of tests
#             v: int  -  number of random samples to print
#                            (default 1%)
#         """

#     v = v if v != 0 else round(v / 100)
#     # samples: List = []
#     samples = [h_num(random.randint(100, 99999000000000000)) for _ in range(n)]
#     print(samples)
#     return 0

if __name__ == "__main__":
    print("nn")
    walk_dir = ''
    if len(sys.argv) > 1:
        walk_dir = sys.argv[1]
    else:
        walk_dir = '*.py'

    print('=> Directory Listing')
    # tests(10, 1)
    dir_list = walk_it(walk_dir, True)
    # print(dir_list)
    # for n in range(25):
    #     print(f"n: {n}    -   {11.482**n}   -    {h_num(11.482**n)}")
# """ old style: python < 3.5

# def walk_it(walk_dir: str) -> int:
#     for root, subdirs, files in os.walk(walk_dir):
#         print('--\nroot = ' + root)
#         list_file_path = os.path.join(root, 'my-directory-list.txt')
#         print('list_file_path = ' + list_file_path)

#         with open(list_file_path, 'wb') as list_file:
#             for subdir in subdirs:
#                 print('\t- subdirectory ' + subdir)

#             for filename in files:
#                 file_path = os.path.join(root, filename)

#                 print('\t- file %s (full path: %s)' % (filename, file_path))

#                 with open(file_path, 'rb') as f:
#                     f_content = f.read()
#                     list_file.write(('The file %s contains:\n' % filename)
#                                     .encode('utf-8'))
#                     list_file.write(f_content)
#                     list_file.write(b'\n')
#     return 0
#     """
