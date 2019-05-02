#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" Binary Patterns """
import math
from os import path
from sys import argv
from typing import Tuple, List
from flask import Flask, jsonify, request

name = argv[0]
here = path.abspath(path.dirname(__file__)) + '/'
css_file = '/static/binary.css'
# css_file = "binary.css"
json_file = here + name + ".json"
app = Flask(__name__)
TR: str = '<tr>'
TRC: str = '</tr>'
TD: str = '<td>'
TDC: str = '</td>'
BR: str = '<br/>'
HR: str = '<hr/>'
NB: str = '&nbsp;'

HEADER = """<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>\n\t\t\tBinary Numbers Test\n\t\t</title>\n\t<link rel = "stylesheet" type = "text/css" href = "{}" /></head>\n\t<body>\n\t\t<div>\n\t\t\t<table>""".format(
    css_file)
FOOTER = """\t\t\t</table>\n\t\t</div>\n\t</body>\n</html>
"""


@app.route("/")
def binary_pattern():
    """ binary numbers tests """
    size: int = 100
    s: str = ''
    color_test: bool = True

    response: str = HEADER + '<tr><td colspan="6">'
    response += 'Binary Numbers Test for numbers up to {}'.format(size)
    response += TDC + TRC
    response += TR
    response += TD + 'Decimal' + TDC
    response += TD + 'Binary' + TDC
    response += TD + '2' + TDC
    response += TD + '3' + TDC
    response += TD + '5' + TDC
    response += TD + '7' + TDC + TRC

    for i in range(2, size):
        color_test = not color_test
        response += "<tr class=\"row_color{}\">".format(int(color_test)) + TD
        response += str(i)

        response += TDC + TD
        response += "{i:>10b}".format(i=i)

        s = "{0:b}".format(i) if i % 2 else ''
        response += TDC + TD + s

        s = "{0:b}".format(i) if i % 3 else ''
        response += TDC + TD + s

        s = "{0:b}".format(i) if i % 5 else ''
        response += TDC + TD + s

        s = "{0:b}".format(i) if i % 7 else ''
        response += TDC + TD + s

        response += TDC + TRC

    response += FOOTER
    return response


if __name__ == "__main__":
    print(here)
    print(name)

    # running REST interface, port=5000 for direct test
    app.run(debug=True, host='127.0.0.1', port=5000)
