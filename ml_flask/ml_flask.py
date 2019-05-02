#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" ml_flask.py """

import os
import pickle
import sys

import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

# name = "ml_flask.py"
name = sys.argv[0]
here = os.path.abspath(os.path.dirname(__file__)) + '/'
json_file = here + name + ".json"
# https://www.youtube.com/watch?v=09JslnY7W_k
reference = "https://towardsdatascience.com/publishing-machine-learning-api-with-python-flask-98be46fb2440"
github_ref = "https://github.com/abaranovskis-redsamurai"
blog_ref = "http://andrejusb.blogspot.com/"
# pylint: disable=unused-variable,eval-used,missing-docstring

# Get headers for payload
headers = [
    'times_pregnant', 'glucose', 'blood_pressure', 'skin_fold_thick',
    'serum_insuling', 'mass_index', 'diabetes_pedigree', 'age'
]

# Use pickle to load in the pre-trained model
with open(here + '/' + 'diabetes-model.pkl', 'rb') as f:
    model = pickle.load(f)

# Test model with data frame
input_variables = pd.DataFrame([[1, 106, 70, 28, 135, 34.2, 0.142, 22]],
                               columns=headers,
                               dtype=float,
                               index=['input'])
# Get the model's prediction
prediction = model.predict(input_variables)
print("Prediction: ", prediction)
prediction_proba = model.predict_proba(input_variables)
print("Probabilities: ", prediction_proba)

app = Flask(__name__)
CORS(app)


@app.route("/katana-ml/api/v1.0/diabetes", methods=['POST'])
def predict():
    payload = request.json['data']
    values = [float(i) for i in payload.split(',')]

    input_variables = pd.DataFrame([values],
                                   columns=headers,
                                   dtype=float,
                                   index=['input'])
    # Get the model's prediction
    prediction_proba = model.predict_proba(input_variables)
    prediction = (prediction_proba[0])[1]

    ret = '{"prediction":' + str(float(prediction)) + '}'

    return ret


# running REST interface, port=5000 for direct test
if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1', port=5000)
