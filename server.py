#import flask
from flask import Flask, url_for, request, abort, redirect, jsonify, session, render_template, url_for

#import the regression model objects
from models import linmodel, polymodel 

app = Flask(__name__, template_folder='static')

#global variables to track model initialization.
lincalled = False
polycalled = False

#index.html
@app.route('/')
def home():
    return render_template('index.html')

#Returns linear model prediction
@app.route('/linear', methods=['POST'])
def linear():
    value = request.form['linValue']

    if value:
        return jsonify({'linValue' : linmodel.predict(float(value))})

    return jsonify({'error' : 'Missing input value!'})

#Returns polynomial model prediction
@app.route('/polynomial', methods=['POST'])
def polynomial():
    value = request.form['polyValue']

    if value:
        return jsonify({'polyValue' : polymodel.predict(float(value))})

    return jsonify({'error' : 'Missing input value!'})

#Initializes the linear model.
@app.route('/linear_init', methods=['GET'])
def linear_init():
    global lincalled
    if lincalled == False:
        linmodel.train()
    
    lincalled = True

    return jsonify({'value' : 'STATUS: Linear Model Loaded.'})

#Initializes the polnomial model.
@app.route('/poly_init', methods=['GET'])
def poly_init():
    global polycalled
    if polycalled == False:
        polymodel.train()
        
    polycalled = True

    return jsonify({'value' : 'STATUS: Polynomial Model Loaded.'})

if __name__ == "__main__":
    app.run() 