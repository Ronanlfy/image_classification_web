from download_model import download
import tensorflow_datasets as tfds
import tensorflow as tf
from tensorflow.keras.applications.imagenet_utils import preprocess_input
import numpy as np

res_net, mobile_net, x_ception = download()

# print(mobile_net.summary())

ds = tfds.load('imagenet2012_subset/1pct', split="train")


class data_gen():
    def __init__(self, shape):
        self.shape = shape
        self.y = []
    def generator(self):
        for example in ds.batch(1):
            x, y = preprocess_input(example["image"]), y, #tf.keras.utils.to_categorical(example["label"], num_classes=1000)
            self.y.append(y)
            yield x, y

train_generator = data_gen(mobile_net.input_shape[1:-1])

mobile_net.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

y_hat = np.argmax(mobile_net.predict(x=train_generator.generator()), axis=1)
y1 = train_generator.y
# y2 = np.argmax(y1, axis=1)
a = 1