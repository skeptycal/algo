#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" walk_dir.py """
# pylint: disable=redefined-outer-name
# flake8: disable=F401
import fileinput
import glob  # python 3.5+
import os
import random
import sys

from typing import List


""" Absolute Path:
    If your current working directory may change during script execution,
    it's recommended to immediately convert program arguments to an absolute
    path. Then the variable root below will be an absolute path as well.

    Example:

    walk_dir = os.path.abspath(walk_dir)

    """


def h_num(n: int) -> str:
    """ convert integer to 'human readable' format """
    # i: float = 0
    if n >= 1024000000000000:
        return str(round(n/(1024 * 10 ** 15), 1)) + ' PB'
    if n >= 1024000000000:
        return str(round(n/(1024 * 10 ** 12), 1)) + ' TB'
    if n >= 1024000000:
        return str(round(n/(1024 * 10 ** 9), 1)) + ' GB'
    if n >= 1024000:
        return str(round(n/(1024 * 10 ** 6), 1)) + ' MB'
    if n >= 1024:
        return str(round(n/(1024 * 10 ** 3), 1)) + ' KB'
    return str(n) + ' B'


def walk_it(walk_dir: str = '**/*', recursive: bool = True):
    """ print directory listing with recursive option """
    filename: str = ''
    for filename in glob.iglob(walk_dir, recursive=recursive):
        # last_dir =
        print(filename)
        print('size of file on disk: ', os.path.getsize(filename))
        st = os.stat(filename)
        print('os.stat of file: ', st)


def tests(n: int, v: int) -> int:
    """ test number formats
            n: int  -  number of tests
            v: int  -  number of random samples to print
                           (default 1%)
        """

    v = round(v/100) if not v else v
    samples: List[str] = [h_num(random.randint(100, 99999000000000000))
                          for _ in range(n)]
    print(samples)
    return 0


if __name__ == "__main__":
    walk_dir: str = ''
    if len(sys.argv) > 1:
        walk_dir = sys.argv[1]
    else:
        walk_dir = '**/*.py'
    print('walk_dir = ' + walk_dir)
    print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
    print('=> Directory Listing')
    walk_it(walk_dir, True)




""" old style: python < 3.5

def walk_it(walk_dir: str) -> int:
    for root, subdirs, files in os.walk(walk_dir):
        print('--\nroot = ' + root)
        list_file_path = os.path.join(root, 'my-directory-list.txt')
        print('list_file_path = ' + list_file_path)

        with open(list_file_path, 'wb') as list_file:
            for subdir in subdirs:
                print('\t- subdirectory ' + subdir)

            for filename in files:
                file_path = os.path.join(root, filename)

                print('\t- file %s (full path: %s)' % (filename, file_path))

                with open(file_path, 'rb') as f:
                    f_content = f.read()
                    list_file.write(('The file %s contains:\n' % filename)
                                    .encode('utf-8'))
                    list_file.write(f_content)
                    list_file.write(b'\n')
    return 0
    """
