import string
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

app = Flask(__name__)
api = Api(app)

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

class sentiment_model(Resource):

    def post(self):
        # print('here in the get method')
        parser = reqparse.RequestParser()  # initialize parser
        parser.add_argument('reqstring', required=True, help='string not correct')  # add args
        args = parser.parse_args() 
        req_string = args['req_string']
        print(args)
        req_tokens = tokenizer.encode(req_string, return_tensors='pt')
        res = model(req_tokens)
        score = int(torch.argmax(res.logits)+1)

        print('sentiment score generated')
        return {'sentiment_score': score}, 200

    def get(self):
        return {'model':str(model),'tokenizer':str(tokenizer)}, 200

api.add_resource(sentiment_model, '/sentiment')

if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app