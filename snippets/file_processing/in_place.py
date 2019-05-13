#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
in_place.py
    In place editing of specific lines

Usage: in_place.py

#   Parameters:
#       [init, -i, --init]        -- install and initialize
#       [commit, -m] MESSAGE      -- git commit and push with MESSAGE
#       [reset, -r, --reset]      -- reset initial repo files (with backup)
#       [version, -v, --version]  -- display version information
#       [help, -h, --help]        -- display usage and information

    """
import fileinput
import sys

from_base = sys.argv[1]
to_base = sys.argv[2]
files = sys.argv[3:]

for line in fileinput.input(files, inplace=True):
    line = line.rstrip().replace(from_base, to_base)
    print(line)


""" References:

https://docs.python.org/2/library/re.html#re.sub
re.sub(pattern, repl, string, count=0, flags=0)

re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
    r'static PyObject*\npy_\1(void)\n{',
    'def myfunc():')

'static PyObject*\npy_myfunc(void)\n{'

"""
