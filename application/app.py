from http.client import NON_AUTHORITATIVE_INFORMATION
from multiprocessing.sharedctypes import Value
from operator import index
from unittest import result
from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Reading data frame from csv file
BASE_DIR = os.getcwd()
csv_path = "global_power_plant_db.csv"
data = pd.read_csv(os.path.join(BASE_DIR, csv_path), low_memory=False)

@app.route('/')
def home():
    return render_template('query.html')

@app.route('/query', methods=['GET', 'POST'])
def query():
    name = request.form['name']
    if name:
        fromPage = (int(name))-1
        resultJSON = (data.iloc[fromPage]).to_json(orient='index', indent=2)
        return(resultJSON)
    return "Page not found", 404
if __name__ == '__main__':
    app.run(host="localhost", port=int("5000"))