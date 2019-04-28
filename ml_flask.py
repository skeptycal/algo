#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" ml_flask.py """

import pickle

import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

name = "ml_flask.py"
json_file = sys.path[0] + '/' + name + ".json"
# https://www.youtube.com/watch?v=09JslnY7W_k
reference = "https://towardsdatascience.com/publishing-machine-learning-api-with-python-flask-98be46fb2440"
# pylint: disable=unused-variable,eval-used,missing-docstring
