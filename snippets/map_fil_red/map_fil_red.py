#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" map_fil_red.py """

import math
# import json
import secrets
# import statistics
import sys
import timeit
from typing import Any, Dict, List, Tuple

import numpy as np

name = "map_fil_red.py"
json_file = sys.path[0] + '/' + name + ".json"
reference = ""
# pylint: disable=unused-variable,eval-used,missing-docstring


def area(r: float) -> float:
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)


def fake_radius_list(n: int = 100, bits: int = 32) -> List[float]:
    """ create a list of fake radii data """
    return [secrets.randbits(bits) for i in range(n + 1)]


test = fake_radius_list(10, 8)
test = list.map('x**0.89', test)
print(test)
