from flask import Flask, request, make_response, jsonify
import os, time
import numpy as np

from flask_cors import CORS

app = Flask(__name__) 

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SECRET_KEY'] = os.urandom(24)

basedir = os.path.abspath(os.path.dirname(__file__))
uploadDir = os.path.join(basedir, 'static/uploads') 
os.makedirs(uploadDir, exist_ok=True)

def address(filename): 
    
    uploadpath = os.path.join(uploadDir, filename)
    return uploadpath

@app.route('/')
def index():
    return {'Value' : 'Welcome'}

@app.route('/test', methods=['GET'])
def test():
    return {'Value' : 'Hello World'}
 
@app.route('/testPost', methods=['POST'])
def testPost():
    print('POST')

    f = request.files['file']
    uploadpath = address(f.filename) 
    f.save(uploadpath)

    res = make_response(jsonify({"message": "OK"}), 200)
    return res

if __name__ == '__main__':

    app.run(debug=True)