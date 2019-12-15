#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" long_hashtags.py - create hashtags from text strings. """
import collections
import os
import random
import sys
import time
from timeit import timeit
from typing import Any, List, Tuple

word_file: str = "/usr/share/dict/words"
with open(word_file) as w:
    WORDS: List[str] = w.read().splitlines()
time_list: Counter = {}
time_list: List[Tuple[str, float]] = []
last_test: List[Tuple[str, float]] = []


def time_tail(t: List[Tuple[str, float]] = time_list, n: int = 2) -> List[Tuple[str, float]]:
    return t[-n:]


def create_word_list(n: int) -> List[str]:

    return [random.choice(WORDS) for _ in range(n)]


def gen_word_list(n: int) -> List[str]:
    yield (random.choice(WORDS) for _ in range(n))


def join_word_list(n: int, sep: str = ',') -> str:
    return sep.join(create_word_list(n))


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        tt = time.time() - ts
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = tt
        else:
            time_list.append((method.__name__, tt))
            # print(f"{method.__name__} {tt:.4f} ms")
        return result
    return timed


def show_comp(t: List[Tuple[str, float]] = time_tail()) -> str:
    # print(f"{t=}")
    if t[0][1] > t[1][1]:
        t = t[::-1]
    slow_label = t[0][0]
    slow_time = t[0][1]
    fast_label = t[1][0]
    fast_time = t[1][1]
    diff = fast_time / slow_time
    return f"{slow_label} is {diff:.2f} times faster than {fast_label}."
    # return 'show_comp'


def hashtag1(_: str) -> str:
    """ convert text string to hashtag """
    return '#' + "".join(_.title().split())


def hashtag(s: str) -> str:
    """ convert text string to hashtag """
    return '#' + "".join(s.title().split())


def hashtag_notitle(s: str) -> str:
    """ convert text string to hashtag """
    return '#' + "".join(s.split())


@timeit
def test_hashtag(s: str, n: int):
    for i in range(n):
        test = hashtag(s)


@timeit
def test_hashtag_notitle(s: str, n: int):
    for i in range(n):
        test = hashtag_notitle(s)


@timeit
def test_hashtag1(s: str, n: int):
    for i in range(n):
        test = hashtag1(s)


def blogtag(s: str, sep: str = ',;') -> str:
    """ convert text string to blog tags (individual tags) """
    s = " #".join(s.title().split(sep=sep))


def tweet(h: str) -> int:
    """ tweet text string """
    return int(h)  # TODO ... temporary return


def main():
    """ main loop - print hashtag and send to clipboard """
    test_str: str = join_word_list(100)
    test_reps: int = 50
    test_cycles: int = 1
    cycle_average: float = 0
    for cycle in range(test_cycles):
        test_hashtag(test_str, test_reps)
        test_hashtag1(test_str, test_reps)
        test_hashtag_notitle(test_str, test_reps)

        # print(f"{time_list=}")
        print(f"{show_comp(time_tail())}")

    # TODO create competing functions and replace default with the fastest function ...
    # TODO   ... then continue on ... through 'generations' of profiling and changes ...
    # TODO   ... to find the best methods to use ... try out any (e.g. dir())

    # s: str = ''
    # if len(sys.argv) < 2:
    #     s = "this is how I create very long hashtags"
    #     print('Testing hashtag generator: ')
    #     print('Test string: ', s)
    # else:
    #     s = ' '.join(sys.argv[1:])
    # s = '#' + "".join(s.title().split())
    # #! SECURITY WARNING:
    # #!   As many people will note, the following line of code
    # #!   can create many security risks. Use wisely and
    # #!   carefully in a controlled environment.
    # os.system("echo '%s' | pbcopy" % s)
    # print(s)
    # print('... copied to clipboard')
    # tweet(s)


if __name__ == "__main__":
    """ testing hashtag generator """
    main()
