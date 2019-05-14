#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" long_hashtags.py - create hashtags from text strings. """
import os
import sys


def hashtag(h: str) -> str:
    """ convert text string to hashtag """
    h = '#' + "".join(h.title().split())
    return h


def tweet(h: str) -> int:
    """ tweet text string """
    pass


def main():
    """ main loop - print hashtag and send to clipboard """
    s: str = ''
    if len(sys.argv) < 2:
        s = "this is how I create very long hashtags"
        print('Testing hashtag generator: ')
        print('Test string: ', s)
    else:
        s = ' '.join(sys.argv[1:])
    s = '#' + "".join(s.title().split())
    #! SECURITY WARNING:
    #! As many people will note, the following line of code
    #!   can create many security risks. Use wisely and
    #!   carefully in a controlled environment.
    os.system("echo '%s' | pbcopy" % s)
    print(s)
    print('... copied to clipboard')
    tweet(s)


if __name__ == "__main__":
    """ testing hashtag generator """
    main()
