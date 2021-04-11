from flask import Flask
APP = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"