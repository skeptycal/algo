""" References:

https://docs.python.org/3.5/library/glob.html#glob.glob

https://stackoverflow.com/questions/2212643/python-recursive-folder-read

If you are using Python 3.5 or above, you can get this done in 1 line.

import glob

for filename in glob.iglob(root_dir + '**/*.txt', recursive=True):
     print(filename)
As mentioned in the documentation

If recursive is true, the pattern '**' will match any files and
zero or more directories and subdirectories.

If you want every file, you can use

import glob

for filename in glob.iglob(root_dir + '**/*', recursive=True):
     print(filename)
"""
