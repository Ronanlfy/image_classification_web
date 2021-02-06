from flask import Flask, request, make_response, jsonify
from werkzeug.utils import secure_filename
import os, time, logging
from tools.inference import classify
from flask_cors import CORS
from tools.load_models import load

models = load()
# import tensorflow as tf
# models["mobilenet_pruned"] = tf.keras.models.load_model("../mobilenet_pruned.h5")

supported_types = ['jpg', 'png'] 

app = Flask(__name__) 

logging.basicConfig(filename='demo.log', level=logging.DEBUG, 
    format='%(asctime)s %(levelname)s %(name)s : %(message)s')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SECRET_KEY'] = os.urandom(24)
 
basedir = os.path.abspath(os.path.dirname(__file__))
uploadDir = os.path.join(basedir, 'static/uploads') 

def address(filename): 
    
    uploadpath = os.path.join(uploadDir, filename)
    return uploadpath

@app.route('/')
def index():
    return 'Welcome! This is the start page of backend.'

@app.route('/test', methods=['GET'])
def test():
    return 'Just a test!'

@app.route('/list_model', methods=['GET'])
def list_model():
    # GET
    # to return all supported models to run prediction with
    app.logger.info('Return supported model lists')

    supported_models = []
    for m in models:
        supported_models.append(m)
    
    return make_response(jsonify({"models": supported_models}), 200)

@app.route('/post_image', methods=['POST'])
def post_image():
    # POST 
    # function to process uploaded image
    app.logger.info('Processing uploaded image')

    f = request.files['file']
    if not os.path.exists(uploadDir):
            os.makedirs(uploadDir) 
    if f:
        filename = f.filename
        if filename.split('.')[-1] in supported_types:
            # save image to backend local disk
            app.logger.info('Processing uploaded image and run prediction.')

            filename = secure_filename(filename)
            uploadpath = address(filename) 
            f.save(uploadpath) 

            chosen_model = request.form['model_name']

            label, score, t = classify(uploadpath, chosen_model, models[chosen_model]) 
            
            print(label, score, t)

            body = {"status": "SUCCESS", "label": label, "score": score, "used_time": str(t)}
            
            res = make_response(body, 200)
        else:
            app.logger.info('Upload image file format is not supported.')
            res = make_response(jsonify({"status": "FAIL", "msg": "Unspported image file format"}), 406)
    else:
        app.logger.info('Upload image is empty.')
        res = make_response(jsonify({"status": "FAIL", "msg": "No file uploaded"}), 400)

    return res

 
if __name__ == '__main__':

    app.run(debug=True)