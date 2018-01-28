from flask import Flask
app = Flask(__name__)
import json
from flask import request, jsonify, render_template

# $ export FLASK_APP=flaskapp.py
# $ flask run

@app.route("/")
def hello():
    return 'Hello World'

if __name__ == "__main__":
    app.run()