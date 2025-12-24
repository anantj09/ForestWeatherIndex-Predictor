from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

lasso_model = pickle.load(open('models/lasso.pkl','rb'))
std_scaler = pickle.load(open('models/scaler.pkl','rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        inputs = {
            'Temperature': request.form.get('Temperature'),
            'RH': request.form.get('RH'),
            'Ws': request.form.get('Ws'),
            'Rain': request.form.get('Rain'),
            'FFMC': request.form.get('FFMC'),
            'DMC': request.form.get('DMC'),
            'ISI': request.form.get('ISI'),
            'Classes': request.form.get('Classes'),
            'Region': request.form.get('Region')
        }

        data_values = [float(x) for x in inputs.values()]
        new_data_scaled = std_scaler.transform([data_values])
        lasso_res = lasso_model.predict(new_data_scaled)[0]    ## as lasso had the best r2 score

        return render_template('home.html', results=round(lasso_res, 2), form_data=inputs)

    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)