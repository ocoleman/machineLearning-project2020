from flask import Flask, url_for, request, abort, redirect, jsonify, session, render_template, url_for

app = Flask(__name__, template_folder='static')



@app.route('/')
def home():
    msg="test"
    return render_template('index.html', msg=msg)


if __name__ == "__main__":
    app.run(debug=True) #allows for realtime editing