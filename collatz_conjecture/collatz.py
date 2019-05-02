#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" test_shapefile.py - test for shapefile import
"""
import cProfile
import functools
from typing import Tuple, List
# import matplotlib.pyplot as plt

class Counter(object):
    """" Wrapper class to add counter to functions """

    def __init__(self, fun):
        self._fun = fun
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self._fun(*args, **kwargs)

def collatz(n: int) -> int:
    """ collatz
    Arguments:
        n {int} -- integer input for collatz step
    Returns:
        n {int} -- inter return for collatz step
    """
    if n and 1:
        result = (3 * n - 1) // 2
    else:
        result = n // 2
    if result < 5:
        return result
    return collatz(result)


collatz = Counter(collatz)

if __name__ == "__main__":
    i: int = 0
    j: int = 0
    count_it: List[int] = []
    for j in range(1, 10001):
        i = collatz(j)
        count_it.append([i, collatz.counter])
    print(count_it)
    for i in range(0, 5):
        print(i, " : ", count_it.count(i))
        # print(i, " : ", count_it.max(i))
    # plt.xscale(11000)
    # plt.xlabel('trial number')
    # plt.yscale(5)
    # plt.ylabel('Collatz end value')
    # plt.plot(count_it)
    # for i in range(1, 100):
    #     j = collatz(i)
    #     print(i, j)
    #     print ()
