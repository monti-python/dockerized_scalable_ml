# -*- coding: utf-8 -*-

from sklearn.externals import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
import gunicorn

app = Flask(__name__)


@app.route("/")
def hello():
 return "Hola amigos!"

@app.route('/predict', methods=['POST'])
def apicall():
    """Receives a JSON containing a list of elements and returns a predicion for each. 
       Mandatory features: sepal_length, sepal_width, petal_length, petal_width
    """
    try:
        # Parse JSON 
        json = request.get_json()
        val = []
        print(json)
        for dic in json:
           val.append([dic['sepal_length'], dic['sepal_width'], dic['petal_length'], dic['petal_width']])

        print(np.array(val))

        # Load model and get prediction
        loaded_model = joblib.load('model/iris_svm_model.pkl')
        y_pred = loaded_model.predict(np.array(val))
        pred_dict = {}
        for i,pred in enumerate(y_pred):
           pred_dict['prediction_'+str(i)] = int(pred)
        responses = jsonify(predictions=pred_dict)
        responses.status_code = 200
    except Exception as e:
        responses = jsonify(predictions={'error':'some error occured, please verify request'})
        responses.status_code = 404
        print ('error', e)
    return (responses)


#if __name__ == "__main__":
# app.run(host='0.0.0.0') # remove debug = True, or set to False
