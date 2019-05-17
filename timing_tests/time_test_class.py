#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" time_test_class.py """
# pylint: disable=redefined-outer-name,missing-docstring
import os
import random
from math import log10, ceil
import sys
from functools import wraps
from pathlib import Path
from time import time
from typing import List, Tuple

BG_COLOR = "[48;5;230m"
HEADER = "[38;5;18m"
BLUE = "[38;5;27m"
PURPLE = "[38;5;92m"
RESET = "[0m"

HUMAN_READABLE: Tuple = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')

TIMER_FORMAT_LONG: str = "=> The function " + BLUE + "{0:<10s}" + RESET + " executed in " + PURPLE + "{1:>10.4f}" + RESET + " seconds."

REPORT_FORMAT: str = "Time for " + BLUE + "{:<.30}" + RESET + "was {:>5.3f} s."


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
            This is 400% faster than str / int conversions and
            somewhat faster than cascasding if statements with division."""
    l = ceil(log10(n)) - 1
    if l > 8:
        l = 8
    return str(round(n / (1.024 * 10**l)), 2) + ' ' + HUMAN_READABLE[l]


class Test(str):
    """ A timing test specification containing a string of source code. """
    # Class Attributes
    time0 = float
    time1 = float

    # Initializer / Instance Attributes
    def __init__(self, name, code):
        """ create a Test object with <name> and <code> """
        self._name: str = name
        self._code: str = code
        self._time: List[float] = ()
        self.time_run

    def get_time(self, avg_test: bool = True) -> float:
        """ Print formatted name and time
            - <avg_test> True for average time
            - <avg_test> False for last time """
        if avg_test:
            sum(self._time) / len(self._time)
        else:
            return self._time[-1]

    def get_time_data(self) -> List[float]:
        """ Return List of time data """
        return self._time

    def time_run(self):
        """ Perform timed test
            - Append time data to list
            - Increment test counter """
        time0 = time()
        exec(self._code)
        time1 = time()
        self._time.append(time1 - time0)

    def print_time(self, avg_test: bool = True):
        """ Print formatted name and time
                <avg_test> True for average time
                <avg_test> False for last time """
        if avg_test:
            print(REPORT_FORMAT.format(self._name, self.get_time(True)))
        else:
            print(REPORT_FORMAT.format(self._name, self.get_time(False)))

    def __repr__(self):
        "print(self.name, ': ', self.code)"
        return super().__repr__()


class CodeTest():
    """ A set of source code tests. """
    count: int = 0
    name: str = ''
    tests: List(Test) = []
    REPORT_FORMAT: str = "Time for {}{:<.30}{} was {:>5.3f}"

    def add_test(self, name: str, code: str) -> bool:
        """ add a test object to the set """
        self.tests.append(Test(name, code))
        pass


if __name__ == "__main__":
    print("nn")

    # print('=> Directory Listing')
    # test_list = ['l = ceil(log10(n))', 's = len(str(n).split(".")[0])']
    # str_a = 'l = ceil(log10(n))'  #! old style
    # str_b = 's = len(str(n).split(".")[0])'  #! old style

    # n = 100000
    # test_a = sum([to_sn_a(431234.1453145) for _ in range(n)])
    # test_b = sum([to_sn_b(431234.1453145) for _ in range(n)])
    # perf_ratio = test_a / test_b
    # if perf_ratio < 1:
    #     perf_ratio = 1 / perf_ratio
    #     t1 = 'B'
    #     t2 = 'A'
    # else:
    #     t1 = 'A'
    #     t2 = 'B'
    # perf_ratio = round(perf_ratio * 100, 1)
    # for test in tests:
    #     print("Time for {}{:<.30}{} was {:>5.3f}".format(
    #         PURPLE, code_str, RESET, test_time))

    # print(test_b)
    # print("Test ",
    #       t1,
    #       " is ",
    #       HEADER,
    #       perf_ratio,
    #       "%",
    #       RESET,
    #       " faster than Test ",
    #       t2,
    #       ".",
    #       sep='')

    # for i in range(10):
    #     n = 11.482**i
    # h = h_num1(n)
    # print("n: ", i, "    n: ", n, "     h_hum(n): ", h)
    # tests(10, 1)
    # dir_list = walk_it(walk_dir, True)
    # print(dir_list)
    # for n in range(25):
    #     print(f"n: {n}    -   {11.482**n}   -    {h_num(11.482**n)}")

#     """
