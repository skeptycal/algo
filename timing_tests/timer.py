#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
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
        print(f'{func.__name__} executed in {end - start:.4f} seconds')
        return result

    return wrapper


# Example: sort some random numbers ...
@timeit
def sort_rnd_num():
    numbers = [random.randint(100, 200) for _ in range(100000)]
    numbers.sort()
    return numbers


numbers = sort_rnd_num()

# >>> numbers = sort_rnd_num()
# sort_rnd_num executed in 0.1880 seconds
