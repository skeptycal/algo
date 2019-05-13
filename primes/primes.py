#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" Binary Patterns Test App"""
import math
import time
import timeit
from functools import reduce
from statistics import mean
from typing import Any, Dict, List


PARAMS_TIME_FLOAT = {'align': ':>', 'pad': '8', 'trunc': '3', 'var_type': 'f'}

def Average_Reduce(lst: List[Any]) -> float:
    """ return average of list values using <functools.reduce> """
    return reduce(lambda a, b: a + b, lst) / len(lst)

def Average_Mean(lst: List[Any]) -> float:
    """ return average of list values using <statistics.mean> """
    return mean(lst)

def Average(lst: List[Any]) -> float:
    """ # Return average of a list using <sum/len> """
    return sum(lst) / len(lst)

def is_prime_v1(n: int) -> bool:
    """ (Version 1) Returns True if n is prime else False """
    if n == 1 or n == 0 or not n % 2:
        return False  # 0 and 1 are not primes
    for d in range(3, n, 2):
        if not n % d:
            return False
    return True

def get_time(c: str) -> float:
    """ Return time needed to execute code
            (using time module)
        Parameters:
            c: str          - string containing code to execute
        Returns:
            float:          - time required to execute
        """
    t0 = time.time()
    exec(c)
    t1 = time.time()
    return t1 - t0

def format_string(align: str = ':>', pad: str = '8', trunc: str = '3', var_type: str = 'f') -> str:
    """ Returns Python 'new style' format string for the given arguments\
            align: str      - one of ':>', ':<', ':^'       (default ':>')\
            pad: int        - number of padding spaces      (default 8)\
            trunc: int      - precision (decimal places)    (default 3)\
            var_type: str   - one of 's', 'd', 'f'          (default 'f')
        """
    # default - PARAMS_TIME_FLOAT = {'align': ':>', 'pad': 8, 'trunc': 3, 'var_type': 'f'}   # (use **PARAMS_TIME_FLOAT)
    return '{' + str(align) + str(pad) + '.' + str(trunc) + str(var_type) + '}'

def print_time(f: float, args, kwargs) -> str:
    """ Wrapper for get_time returns string with message. """
    c_format = 'Time required: ' + format_string(args, kwargs) + 's.'
    return c_format.format(f)

def loop_trials(c: str, n: int = 100) -> List[float]:
    """ Return list of times for <n> trials executing code <c>. """
    return [get_time(c) for _ in range(n - 1)]

def test_loops(c: str, n: int = 100, params_str: Dict[str,str] = PARAMS_TIME_FLOAT):
    pass


def main():
    """ Main Loop for Program """
    l: List[int] = [] # just a list to have around ...

    #* Test timing loops for quadratics
    n: int = 100 # number of trials
    str_n: str = "[_**2 for _ in range({})]".format(n)
    print("    ", str_n)
    print(get_time(str_n))

    print("test for x**2 when x = {}".format(n))
    l = loop_trials(str_n, n)
    print(mean(l))


    #* Test timing loops for primes
    p: int = 100
    primes_str = "[is_prime_v1(_) for _ in range({})]".format(p)
    primes: List[bool] = [is_prime_v1(i) for i in range(p)]

    print(print_time(get_time(primes_str), **PARAMS_TIME_FLOAT))

    l = [_**2 for _ in range(10)]
    x = sum(l)


if __name__ == "__main__":
    main()

# * Tests

# print([is_prime_v1(_) for _ in range(10000)])
# print (format_string(**PARAMS_TIME_FLOAT))


# References:
# https://en.wikipedia.org/wiki/Primality_test
# https://www.comeausoftware.com/2016/11/first-steps-python-prime-numbers/
# https://www.geeksforgeeks.org/python-program-for-efficient-program-to-print-all-prime-factors-of-a-given-number/
