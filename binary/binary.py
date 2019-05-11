#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" Binary Patterns Test App"""
import argparse
import json
import math
import multiprocessing
import pathlib
from os import path  # ? update to pathlib
from sys import argv
from typing import Any, Dict, List

import jedi
import requests

from flask import (Flask, flash, jsonify, redirect, request,
                   send_from_directory, url_for)
from werkzeug.utils import secure_filename
from werkzeug.wsgi import SharedDataMiddleware

# Import information ...
# flaskext.mysql - https://stackoverflow.com/questions/45162025/using-mysql-with-flask
# werkzeug.utils - http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
# werkzeug.wsgi - https://werkzeug.palletsprojects.com/en/0.15.x/middleware/shared_data/

name = argv[0]
here = path.abspath(path.dirname(__file__)) + '/'
css_file = './static/binary.css'  # ? add to config.json file
json_file = './static/binary.json'  # ? add to config.json file
header_file = './static/header.html'
footer_file = './static/footer.html'


app = Flask(__name__)

TR: str = '<tr>'
TRC: str = '</tr>'
TD: str = '<td>'
TDC: str = '</td>'
BR: str = '<br/>'
HR: str = '<hr/>'
NB: str = '&nbsp;'


# HEADER = '{}'.format(header_file)

HEADER = """<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>\n\t\t\tBinary Numbers Test\n\t\t</title>\n\t<link rel = "stylesheet" type = "text/css" href = "{}" /></head>\n\t<body>""".format(
    css_file)
FOOTER = """</body>\n</html>
"""

@app.route("/")
def binary_pattern():
    """ binary numbers tests """
    size: int = 100
    s: str = ''
    color_test: bool = True

    response: str = HEADER + '\n\t\t<div>\n\t\t\t<table><tr><td colspan="6">'
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
    # response += '<tr><td colspan="6">'
    # response += '<embed src="https://wakatime.com/share/@skeptycal/a3be8384-4763-47e5-99c6-094cca93b838.svg" width=20%></embed>'
    # response += TDC + TRC
    response += '\t\t\t</table>\n\t\t</div>\n\t'
    response += FOOTER
    return response


if __name__ == "__main__":
    name = argv[0]
    here = path.abspath(path.dirname(__file__)) + '/'
    print('argv[0]: ',name)
    print('here(os.path): ', here)
    print('pathlib.cwd(): ', pathlib.Path.cwd())


    # running REST interface, port=5000 for direct test
    app.run(debug=True, host='127.0.0.1', port=5000)
