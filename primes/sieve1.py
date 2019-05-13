#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" Binary Patterns Test App"""
import math
import time
import timeit
from typing import Any, Dict, List

def primes_sieve2(limit: int = 10000) -> bool:
    a: List[bool] = [True] * limit   # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

                # use 2 rad 3 for sqrt(12) in sqrt series / irrational series

def get_primes(n: int = 10000)->List[int]:
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

n: int = 10000
primes_sieve2(n)[-1]
print(get_primes(n)[-1])


# 1.1499958793645562

# References:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# https://en.wikipedia.org/wiki/Algorithm
# https://stackoverflow.com/questions/2897297/speed-up-bitstring-bit-operations-in-python
#
