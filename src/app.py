from flask import Flask, request
import os, time
import numpy as np

from flask_cors import CORS

app = Flask(__name__) 

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    return {'Value' : 'Welcome'}

@app.route('/test', methods=['GET'])
def test():
    return {'Value' : 'Hello World'}
 
 
if __name__ == '__main__':

    app.run(debug=True)