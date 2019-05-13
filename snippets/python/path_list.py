#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" file_lines.py - print the number of lines
        of python code in a directory. """

import os

YOUR_DIRECTORY = "**./*"
files = [
       os.path.join(parent, name)
       for (parent, subdirs, files) in os.walk(YOUR_DIRECTORY)
       for name in files + subdirs
   ]

""" References:

https://stackoverflow.com/questions/2212643/python-recursive-folder-read

If you want a flat list of all paths under a given dir
(like find . in the shell):

   files = [
       os.path.join(parent, name)
       for (parent, subdirs, files) in os.walk(YOUR_DIRECTORY)
       for name in files + subdirs
   ]
To only include full paths to files under the base dir, leave out + subdirs.
"""
