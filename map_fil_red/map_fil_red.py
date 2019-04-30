#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" map_fil_red.py """

import math
# import json
import secrets
# import statistics
# import sys
import timeit
from typing import Any, Dict, List, Tuple

import numpy as np

name = "map_fil_red.py"
json_file = sys.path[0] + '/' + name + ".json"
# https://www.youtube.com/watch?v=09JslnY7W_k
reference = "https://www.youtube.com/watch?v=09JslnY7W_k"
# pylint: disable=unused-variable,eval-used,missing-docstring


def area(r: float) -> float:
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)


def fake_radius_list(n: int = 100) -> List(float):
    """ create a list of fake radii data """
    return [secrets. for i in range(n + 1)]
