from flask import Flask, request, jsonify
import pickle
import numpy as np


def loadall(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break


with open('./models/diplom_pipeline.pkl', 'rb') as pkl_file:
    model = loadall(pkl_file)

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json.get('features'))
    features = features.reshape(1, 10)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction[0]})


if __name__ == '__main__':
    app.run('localhost', 5000)
