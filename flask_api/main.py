from flask import Flask, request

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# create the Flask app
app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

response_dir = {1:'Comeone man, you dont have to be mean now',2:'Not cool man',3:'Mehh, you can do better',4:'Thanks for the compliment mate',5:'Thats what I\'m taking about'}

@app.route('/query-sentiment')
def query_example():
    req_string = request.args.get('reqstring')
    if(req_string == '' or req_string==" "):
        return {'response':'an empty string was passed so far'},200
    print(req_string)
    req_tokens = tokenizer.encode(req_string, return_tensors='pt')
    res = model(req_tokens)
    score = int(torch.argmax(res.logits)+1)

    print('sentiment score generated')
    return {'response': response_dir[score],'sentiment_score':score}, 200
    # return "<h1>{}</h1>".format(response_dir[score]), 200

@app.route('/model-description')
def form_example():
    return {'model':str(model),'tokenizer':str(tokenizer)}

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)