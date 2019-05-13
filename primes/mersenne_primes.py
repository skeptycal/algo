#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" Binary Patterns Test App"""
from typing import List

# https://en.wikipedia.org/wiki/Mersenne_prime
def Mersenne_primes(n: int) -> List[int]:
    return [2 ** _ - 1 for _ in range(1,n)]

x = Mersenne_primes(10000)
print(x[-1])
