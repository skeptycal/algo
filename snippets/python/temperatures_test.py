#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" temperatures_test.py """

import json
import secrets
import statistics
import sys
import timeit
from typing import Any, Dict, List, Tuple

import numpy as np

name = "temperatures_test.py"
json_file = sys.path[0] + '/' + name + ".json"
# https://www.youtube.com/watch?v=09JslnY7W_k
reference = "https://www.youtube.com/watch?v=09JslnY7W_k"
# pylint: disable=unused-variable,eval-used,missing-docstring

cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
