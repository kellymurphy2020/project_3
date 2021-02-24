# Import dependencies
from flask import Flask
import pandas as pd
import json
import numpy as np
from flask_restful import Api
import predict
import requests
import os
from sqlalchemy import create_engine
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

# Create APP
app = Flask(__name__)
API = Api(app)
# Import dependencies
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/district_db")
Base = automap_base()
Base.prepare(engine, reflect=True)

#1 API predict arson midland
API.add_resource(predict.Predict_arson, '/predict_arson_midland1')

@app.route('/predict_arson_midland/<month_ahead_arson>')
def get_prediction_arson(month_ahead_arson=1):
    url = 'http://127.0.0.1:5000/predict_arson_midland1'
    body = {
        "month_ahead_arson": month_ahead_arson,
    }
    response = requests.post(url, data=body)
    return response.json()

#2 API predict fraud perth
API.add_resource(predict.Predict_fraud, '/predict_fraud_perth')

@app.route('/predict_fraud_perth/<month_ahead_fraud>')
def get_prediction_fraud(month_ahead_fraud=1):
    url = 'http://127.0.0.1:5000/predict_fraud_perth'
    body = {
        "month_ahead_fraud": month_ahead_fraud,
    }
    response = requests.post(url, data=body)
    return response.json()

#3 API predict murder mirrabooka
API.add_resource(predict.Predict_murder, '/predict_murder_mirrabooka1')

@app.route('/predict_murder_mirrabooka/<month_ahead_murder>')
def get_prediction_murder(month_ahead_murder=1):
    url = 'http://127.0.0.1:5000/predict_murder_mirrabooka1'
    body = {
        "month_ahead_murder": month_ahead_murder,
    }
    response = requests.post(url, data=body)
    return response.json()

#4 API predict assault on police kimberley
API.add_resource(predict.Predict_assault, '/predict_assault_police_kimberley1')

@app.route('/predict_assault_police_kimberley/<month_ahead_assault>')
def get_prediction_assault(month_ahead_assault=1):
    url = 'http://127.0.0.1:5000/predict_assault_police_kimberley1'
    body = {
        "month_ahead_assault": month_ahead_assault,
    }
    response = requests.post(url, data=body)
    return response.json()

#5 API predict drugs joondalup
API.add_resource(predict.Predict_drugs, '/predict_drugs_joondalup1')

@app.route('/predict_drugs_joondalup/<month_ahead_drugs>')
def get_prediction(month_ahead_drugs=1):
    url = 'http://127.0.0.1:5000/predict_drugs_joondalup1'
    body = {
        "month_ahead_drugs": month_ahead_drugs,
    }
    response = requests.post(url, data=body)
    return response.json()

#Random: API get all crime data
@app.route("/api/crime")
def getCrime():
    dbConnect = engine.connect()
    df = pd.read_sql('select * from crime', dbConnect)
    jsonData= json.loads(df.to_json(orient='records'))
    dbConnect.close()
    return jsonify(jsonData)

if __name__ == '__main__':
    app.run(debug=True, port='80')
