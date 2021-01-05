from flask import Flask, url_for, request, abort, redirect, jsonify, session, render_template, url_for
from models import linmodel
app = Flask(__name__, template_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/linear', methods=['POST'])
def linear():
    value = request.form['linValue']

    if value:
        return jsonify({'linValue' : linmodel.predict(float(value))})

    return jsonify({'error' : 'Missing input value!'})


if __name__ == "__main__":
    app.run() #allows for realtime editing