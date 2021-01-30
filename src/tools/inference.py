import time
import numpy as np
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from .preprocessing import preprocess_data, load_image


def classify(uploadpath, model):

    start = time.time()
    x_predict = preprocess_data(uploadpath, model.input_shape[1:])

    result = model.predict(x_predict)  
    end = time.time()
    pred = decode_predictions(result, top=3)

    return pred, end - start
