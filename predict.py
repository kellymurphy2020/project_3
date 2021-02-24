from flask_restful import Api, Resource, reqparse
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import json

# Create predict method for arson
class Predict_arson(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('month_ahead_arson')
        # Convert input data to array
        x_model = ARIMA([1,0,1,1,1], order=(1,1,2))
        existing_model = x_model.fit().load('arson_midland.model')
        prediction_arson=existing_model.forecast(24)        
        # Generate prediction for a single value
        out = {'Prediction': json.dumps(prediction_arson.tolist())}
        return out, 200

# Create predict method for fraud
class Predict_fraud(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('month_ahead_fraud')
        # Convert input data to array
        x_model = ARIMA([1,0,1,1,1], order=(1,1,2))
        existing_model = x_model.fit().load('fraud_perth.model')
        prediction_fraud=existing_model.forecast(24)        
        # Generate prediction for a single value
        out = {'Prediction': json.dumps(prediction_fraud.tolist())}
        return out, 200

# Create predict method for murder
class Predict_murder(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('month_ahead_murder')
        # Convert input data to array
        x_model = ARIMA([1,0,1,1,1], order=(1,1,2))
        existing_model = x_model.fit().load('murder_mirrabooka.model')
        prediction_murder=existing_model.forecast(24)        
        # Generate prediction for a single value
        out = {'Prediction': json.dumps(prediction_murder.tolist())}
        return out, 200


# Create predict method for assault on police
class Predict_assault(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('month_ahead_assault')
        # Convert input data to array
        x_model = ARIMA([1,0,1,1,1], order=(1,1,2))
        existing_model = x_model.fit().load('assault_police_kimberley.model')
        prediction_assault=existing_model.forecast(24)        
        # Generate prediction for a single value
        out = {'Prediction': json.dumps(prediction_assault.tolist())}
        return out, 200

# Create predict method for drug offences
class Predict_drugs(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('month_ahead_drugs')
        # Convert input data to array
        x_model = ARIMA([1,0,1,1,1], order=(1,1,2))
        existing_model = x_model.fit().load('drugs_joondalup.model')
        prediction_drugs=existing_model.forecast(24)        
        # Generate prediction for a single value
        out = {'Prediction': json.dumps(prediction_drugs.tolist())}
        return out, 200
