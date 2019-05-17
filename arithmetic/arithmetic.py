#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" arithmetic.py """
import math
# pylint: disable=redefined-outer-name,missing-docstring
import os
import random
import sys
from typing import List, Dict
from functools import wraps
from pathlib import Path
from time import time

BG_COLOR = "[48;5;230m"
HEADER = "[38;5;18m" + BG_COLOR
BLUE = "[38;5;27m" + BG_COLOR
PURPLE = "[38;5;92m" + BG_COLOR
RESET = "[0m"


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


def test_method(n: int, s: str) -> float:
    """ return time to run <n> iterations of <s> method """
    time0 = time()
    for i in range(n):
        exec(s)
    time1 = time()
    return time1 - time0


def get_operators() -> List:
    return ['+', '-', '*', '/']


def test_answer(n, a) -> float:
    return n / a


def seek(inputs, answers) -> str:
    operators = get_operators


def main():
    answers = [i**2 for i in range(20)]
    inputs = [i for i in range(20)]
    algorithm = seek(inputs, answers)
    return


if __name__ == "__main__":
    main()
