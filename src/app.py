from flask import Flask, request, make_response, jsonify
import os, time
import numpy as np
from tools.load_models import load
from tools.inference import classify, classify_with_quantified
from flask_cors import CORS

from tools.load_models import load

models = load()

supported_types = ['jpg', 'png'] 

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

@app.route('/list_model', methods=['GET'])
def list_model():

    supported_models = []
    for m in models:
        supported_models.append(m)
    
    return make_response(jsonify({"models": supported_models}), 200)

@app.route('/testPost', methods=['POST'])
def testPost():

    f = request.files['file']
    if not os.path.exists(uploadDir):
            os.makedirs(uploadDir) 
    if f:
        filename = f.filename
        if filename.split('.')[-1] in supported_types:
            uploadpath = address(filename) 
            f.save(uploadpath) 

            #TODO: get the which model to run prediction
            # chosen_model = request.body["model"]
            chosen_model = "mobilenet_int8"

            pred, t = classify(uploadpath, chosen_model, models[chosen_model]) 
            
            print(pred, t)
            _, prediction, probability = pred[0][0]

            res = make_response(jsonify({"status": "SUCCESS", "prediction": str(prediction), 
                                    "likelihood": str(probability), "used_time": str(t)}), 200)
        else:
            res = make_response(jsonify({"status": "FAIL", "msg": "Unspported image file format"}), 406)
    else:
        res = make_response(jsonify({"status": "FAIL", "msg": "No file uploaded"}), 400)

    return res

if __name__ == '__main__':

    app.run(debug=True)