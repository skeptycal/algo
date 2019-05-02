""" extract date and time """
# answer to Stack Overflow question ...
import re


def convert_to_datetime(line: str):
    match = re.search('\d{4}-\d{2}-\d{2}', line.strip('T')).group()
    match += ' | ' + re.search('\d{2}:\d{2}:\d{2}', line).group()
    return match


def cut_out_datetime(line: str):
    line = re.sub('ERROR ', "", line)
    line = re.sub('T', " | ", line)
    return line


s = 'ERROR 2019-02-03T23:21:20'
print('   Test string: ', s)
print()
print('Extract method: ', convert_to_datetime(s))
print(' "Trim" method: ', cut_out_datetime(s))
"""
OUTPUT:
   Test string:  ERROR 2019-02-03T23:21:20

Extract method:  2019-02-03 | 23:21:20
 "Trim" method:  2019-02-03 | 23:21:20

[Done] exited with code=0 in 0.05 seconds
"""
