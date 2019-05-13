#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" replace CR with LF """
import sys
import fileinput


# for line in fileinput.input(mode='rU'):

with fileinput.input(mode='rU'):
    for line in f:
        process(line)

# with fileinput.input((mode='rU')):

# sys.stdout.writelines(
#     line.replace('\r', '\n') for line in fileinput.input(mode='rU'))
