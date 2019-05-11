#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" Binary Patterns Test App"""
import json
import math
from os import path  # TODO update to pathlib
from sys import argv
from typing import Any, Dict, List

from config import Config
from flask import (Flask, flash, jsonify, redirect, request,
                   send_from_directory, url_for)
from flaskext.mysql import MySQL
from werkzeug.utils import secure_filename
from werkzeug.wsgi import SharedDataMiddleware

# Import information ...
# flaskext.mysql - https://stackoverflow.com/questions/45162025/using-mysql-with-flask
# werkzeug.utils - http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
# werkzeug.wsgi - https://werkzeug.palletsprojects.com/en/0.15.x/middleware/shared_data/

name = argv[0]
here = path.abspath(path.dirname(__file__)) + '/'
css_file = './static/binary.css'  # TODO add to config.json file
json_file = "./static/binary.json"  # TODO add to config.json file
app = Flask(__name__)
app.config.clear

# class app
# path to upload UPLOAD_FOLDER; # TODO add to config.json file
UPLOAD_FOLDER = '/path/to/the/uploads'
# allowed upload types # TODO add to config.json file
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# storage location for uploaded files # TODO add to config.json file
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# 16 MB upload filesize limit; larger raises RequestEntityTooLarge exception
# TODO add to config.json file
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.add_url_rule('/uploads/<filename>', 'uploaded_file', build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app,
                                    {'/uploads': app.config['UPLOAD_FOLDER']})

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'  # TODO add to config.json file
app.config[
    'MYSQL_DATABASE_PASSWORD'] = '******'  # TODO add to config.json file
app.config['MYSQL_DATABASE_DB'] = 'shop'  # TODO add to config.json file
app.config['MYSQL_DATABASE_HOST'] = 'localhost'  # TODO add to config.json file
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


def allowed_file(filename) -> bool:
    """ test for allowed file format """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """ display uploaded file """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """ upload file from client """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


class DevelopmentConfig():
    """ Dev Config for cloud storage """

    # https://github.com/mardix/flask-cloudy
    def get_json(self, file: str = json_file) -> Dict:
        """ Get program info from json file. """
        try:
            with open(file, "r") as read_file:
                data = json.load(read_file)
        except IOError as e:
            return e.args[0]
        else:
            return data

    def put_json(self, data: Dict, file: str = json_file) -> int:
        """ Write program info to json file. """
        try:
            with open(file, "w") as write_file:
                json.dump(data, write_file)
        except IOError as e:
            return e.args[0]
        else:
            return 0

    def create_usage(self, data: Dict) -> str:
        """ Create program usage info from json file. """
        self.USAGE = data['usage']
        return self.USAGE

    def create_version(self, data: Dict) -> str:
        """ Create program version info from json file. """
        self.VERSION = data['version']
        return self.VERSION

    @staticmethod
    def status(s):
        """Prints CLI string in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def print_version_string(self) -> str:
        self.status('Binary Tester Version' + self.VERSION)

    def get_key(self, key_name: str) -> Any:
        jsonify()
        pass

    def get_provider_details(self, storage_provider_choice: str) -> bool:
        """ get storage provider details from json file """
        self.STORAGE_PROVIDER = storage_provider_choice
        self.STORAGE_KEY = self.get_key('STORAGE_KEY')
        self.STORAGE_SECRET = self.get_key('STORAGE_KEY')
        SECRET_KEY = 'I_will_never_told_you'
        STORAGE_CONTAINER = "./data"
        STORAGE_KEY = ""
        STORAGE_SECRET = ""
        STORAGE_SERVER = True

    def change_provider(self, storage_provider_choice: str = 'LOCAL') -> bool:
        """ change to a different storage provider; return success status """
        self.STORAGE_PROVIDER = storage_provider_choice
        return True

    def __init__(self,
                 json_config_file: str,
                 storage_provider_choice: str = 'LOCAL',
                 debug_choice: bool = True):
        """ setup storage with default LOCAL """
        self.CONFIG_FILE = json_config_file
        self.CONFIG: Dict[Any] = self.get_json(self.CONFIG_FILE)
        self.VERSION = self.CONFIG('version')
        self.DEBUG = debug_choice
        self.STORAGE_PROVIDER = storage_provider_choice
        self.STORAGE_KEY = ''
        self.STORAGE_SECRET = ''
        self.SECRET_KEY = 'I_will_never_told_you'
        self.STORAGE_CONTAINER = "./data"
        self.STORAGE_KEY = ""
        self.STORAGE_SECRET = ""
        self.STORAGE_SERVER = True
        return


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
