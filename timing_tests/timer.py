#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" testing <timeit> wrapper """
import random
from functools import wraps
from time import time

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
def sort_rnd_num():
    """ # Example: sort some random numbers ... """
    number_list = [random.randint(100, 200) for _ in range(100000)]
    number_list.sort()
    return number_list


numbers = sort_rnd_num()

# >>> numbers = sort_rnd_num()
# sort_rnd_num executed in 0.1880 seconds
