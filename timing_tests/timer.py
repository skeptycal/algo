#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" testing <timeit> wrapper """
import random
from functools import wraps
from time import time


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
        print(f'=> The function {func.__name__} executed in {end - start:.4f} seconds.')
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
