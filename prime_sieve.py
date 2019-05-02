#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# # Prime Number Sieve
# http://inventwithpython.com/hacking (BSD Licensed)
# https://inventwithpython.com/hacking/chapter23.html

import math
from typing import Tuple, List


def isPrime(num):
    """ # Returns True if num is a prime number, otherwise False.
        # Note: Generally, isPrime() is slower than primeSieve().
        # all numbers less than 2 are not prime """
    if num < 2:
        return False
    # see if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def primeSieve(sieveSize: int = 10000) -> List[int]:
    # Returns a list of prime numbers calculated using
    # the Sieve of Eratosthenes algorithm.
    sieve = [True] * sieveSize
    sieve[0] = False  # zero and one are not prime numbers
    sieve[1] = False
    # create the sieve
    # for i in range(2, int(math.sqrt(sieveSize)) + 1):
    #     pointer = i * 2
    #     while pointer < sieveSize:
    #         sieve[pointer] = False
    #         pointer += i

    r: int = int(math.sqrt(sieveSize)) + 1
    sieve.extend([i * 2 for i in range(2, r)])
    # compile the list of primes
    primes = []
    primes.extend([i for i in range(sieveSize) if sieve[i]])
    return primes


if __name__ == "__main__":
    size: int = 1000
    prime_list: List[int] = primeSieve(size)
    print(prime_list)
    print('Largest prime below {} is {}.'.format(size, prime_list[-1]))
