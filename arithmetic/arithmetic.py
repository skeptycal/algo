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
from typing import List, Dict

BG_COLOR = "[48;5;230m"
HEADER = "[38;5;18m" + BG_COLOR
BLUE = "[38;5;27m" + BG_COLOR
PURPLE = "[38;5;92m" + BG_COLOR
RESET = "[0m"

TIMER_FORMAT = "=> The function " + BLUE + "{0:<10s}" + RESET + " executed in " + PURPLE + "{1:>10.4f}" + RESET + " seconds."


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
        print(TIMER_FORMAT.format(func.__name__, end - start))
        return result

    return wrapper


@timeit
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


def test_answers(n: int, f: str) -> dict(int, int):
    return {{i: i**2} for i in range(2000)}


if __name__ == "__main__":
    answers: dict() = test_answers(20, 'x ** 2')
    print(answers)
