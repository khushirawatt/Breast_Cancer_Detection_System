from flask import Flask, request, render_template
import pandas  as pd
import numpy as np
import pickle


model = pickle.load(open('models/model.pkl', 'rb'))

#flask app

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods = ['POST'])
def predict():
    features = request.form['feature']
    features = features.split(',')
    np_features = np.asarray_lst(features_lst,dtype = np.float32)
    pred = model.predict(np_features.reshape(1,-1))

    output = ['Cancrouse' if pred[0] == 1 else 'Not Cancrouse']

    return render_template('index.html', message = message)

#python main
if __name__ == '__main__':
    app.run(debug=True)
     


