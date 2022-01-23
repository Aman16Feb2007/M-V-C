from flask import Flask, jsonify, request
from classifier import get_prediction
import random

app = Flask(__name__)

@app.route('/predict-alpha', methods = ['POST'])
def predict_digit():
    image = request.files.get('alphabet')
    prediction = get_prediction(image)
    return jsonify({
        'prediction' : prediction
    }), 200

if(__name__ == '__main__'):
    r = random.randint(1000, 9999)
    app.run(debug=True, port=r)