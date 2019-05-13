#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" Mersenne_sequence.py """

import json
import secrets
import statistics
import sys
import timeit
from typing import Any, Dict, List, Tuple

import numpy as np

name = "Mersenne_sequence.py"
json_file = sys.path[0] + '/' + name + ".json"
# https://www.youtube.com/watch?v=09JslnY7W_k
reference = "https://www.youtube.com/watch?v=09JslnY7W_k"
# pylint: disable=unused-variable,eval-used,missing-docstring


def get_json(file: str = json_file) -> Dict:
    """ Get program info from json file. """
    with open(file, "r") as read_file:
        data = json.load(read_file)
    return data


def put_json(data: Dict, file: str = json_file) -> int:
    """ Write program info to json file. """
    with open(file, "w") as write_file:
        json.dump(data, write_file)
    return 0


def create_usage(data: Dict) -> str:
    """ Create program usage info from json file. """
    usage = data['usage']
    return usage


def create_version(data: Dict) -> str:
    """ Create program version info from json file. """
    usage = data['version']
    return usage


class Mersenne_Sequence(object):
    """ Calculate n iterations of a Mersenne Sequence
        n {int}      -- number of iterations in series
        f {str}      -- formula in 'python math .format string'
             (e.g.) '{x}**2 + 1'
        return {int} -- integer result of sequence
        """

    def __init__(self, f: str, n: int = 10, r: int = 5000):
        self.n: int = n
        self.f: str = f
        self.r: int = r
        self.timer_setup: str = 'from __main__ import timer'
        self.npa: np.ndarray

    def update_parameters(self, f: str, n: int, r: int) -> int:
        self.f = f
        self.n = n
        self.r = r
        return 0

    def time_fn(self, fn: Any, setup: str, number) -> List[float]:
        """ time a function """
        return timeit.repeat(fn, setup, number)

    def mersenne_1(self) -> int:
        # Generator comprehension version
        # iteration = (eval(f.format(_)) for _ in range(n))
        return sum((eval(self.f.format(_)) for _ in range(self.n)))

    def mersenne_2(self) -> int:
        # List comprehension version
        # iteration = [eval(f.format(_)) for _ in range(n)]
        return sum([eval(self.f.format(_)) for _ in range(self.n)])

    def mersenne_3(self) -> int:
        # traditional list loop version
        # iteration = for _ in range(n): y.append(eval(f.format(_)))
        y: List = []
        for _ in range(self.n):
            y.append(eval(self.f.format(_)))
        return sum(y)

    def mersenne_4(self) -> int:
        # numpy  comprehension version
        pass


    def switch_mersenne(self, argument):
        """
            switch_mersenne - choose algorithm to test

            argument: int   - used to create method name
        """
        method_name = 'mersenne_' + str(argument)
        print(method_name)  # ! Test
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: None)
        print(method)  # ! Test
        # Call the method as we return it
        # n: int, f: str, r: int
        return method()


def mainloop() -> int:
    """ Main Loop
        n - number of iterations in series
        f - string with formula in python eval format
        r - repeats for each iteration set
        """
    f: str = "2 * {} + 1"
    n: int = 12
    r: int = 5000
    times: Dict = {}
    Mers: Mersenne_Sequence = Mersenne_Sequence(f, n, r)
    return 0


# cli_main
if __name__ == "__main__":

    def g(x: int) -> int:
        return x * x

    m: float = statistics.mean(
        timeit.repeat("for x in range(100): g(x)",
                      "from __main__ import g",
                      number=10000))

    print('Average of 5 trials: {0:.{1}f}'.format(m, 3))

    mainloop()

#
""" # TODO need to parse this
    # 1) generator comp. 2) list comp. 3) traditional loop
    # strait through, messy linear code
    # 'for i in range(10000), reset m = 0, typeset m:int = 0 in loop'
        0.6837670803070068 # *this is 38% slower with one iteration
        0.7040719985961914
        0.7379920482635498
    # no typeset m:int
        0.7070600986480713
        0.726517915725708   # gradual slowdown
        0.791165828704834   # much slower
    # no reset m = 0 or typeset
        0.7733209133148193  # slowdown
        0.7549538612365723  # gradual slowdown
        0.8000099658966064
    # use _ instead of i + all above
        0.7171399593353271  # big improvement
        0.7672159671783447
        0.7385678291320801  # big improvement
    # best of these: _ and typeset m:int = 0 in loop
        0.6679959297180176
        0.6514832973480225
        0.6654109954833984
    # + all loop variables replaced with _
        0.6210191249847412
        0.6191449165344238
        0.6387639045715332

    # using function calls from switch function

"""
