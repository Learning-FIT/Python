from flask import Flask, request, Response
import pickle
import json

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    json_data = request.get_json()

    with open('model.pickle', mode='rb') as fp:
        model = pickle.load(fp)
    pred = model.predict([[json_data['value']]])

    result = {
        'result': pred[0][0]
    }

    return Response(json.dumps(result), content_type='application/json')
