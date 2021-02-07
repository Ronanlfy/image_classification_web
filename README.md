# web_classification

This repo is to set up a simple web page to run oneline image classification. And it focuses on a speeding up inference with quantization and model pruning. It includes a frontend (built in .js) and a backend (built with python, Flask), communicating through rest API. Frontend will display all supported models and upload image to backend to run prediction. And the backend is reponsible for preprocessing, model prediction and return result.

## Setup ##

The following setup has been tested with Windows Cygwin and Linux.

1. clone this project https://github.com/Ronanlfy/web_classification.git

2. go to dir where you save this repo

3. run the setup.sh by `$bash setup.sh` to set up working virtual-env and install required packages.

4. start the backend by `$bash run_backend.sh`, the first time will take slightly long time.

5. wait for step 4 finish, open Chrome and go to page http://localhost:5000/ to double-check if the backend is up and running. If it says "Welcome! This is the start page of backend.", now you are free to move on!

6. open `/src/frontend/index.html` on Chrome, now you can upload image and start testing!

## Week 1 ##

### Frontend ###

Build frontend where user can choose model and image to run prediction with, and prediction with best accuracy is returned.

![frontend](images/frontend/frontend.png)

### Backend ###

1. Build Flask app to recieve API calls from frontend, including get all supported models and also run prediction with uploaded images.

2. Add Mobilnet, Resnet50, and Xception as supported models.

3. Add three models mentioned above and corresponding float16, int6 quanatized versions.

### Result ###

This chart is obtained from running prediction on win10 once. It displays the probablity (for original and float16 models) and running time to predict a given image. So depends on the hardware, result on running time might vary a lot for each run:

| images \ prediction, time (seconds) | Resnet | Resnet float16 | Resnet int8 | Xception | Xception float16 | Xception int8 | mobilenet | mobilenet float16 | mobilenet int8 |
| -----:|------:| -----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|
|images/test_images/cat.png  | tabby, 0.89s|tabby, 0.66s| tabby, 47s|tabby, 1.07s|tabby, 0.69s|tabby, 282s|tabby, 0.68s|tabby, 0.56s|tabby, 7.5s|
|images/test_images/dog.png     | Great_Pyrenees, 0.47s|Great_Pyrenees, 0.36s|Great_Pyrenees, 45s|white_wolf, 0.57s|white_wolf, 0.55s| white_wolf, 253s|Eskimo_dog, 0.34s|Eskimo_dog, 0.17s|Eskimo_dog, 5.8s|

Int8 models run pretty slow, which might be expected since tflite is more optimized on mobile/embedded (e.g. arm). Check out more discussions [here](https://github.com/tensorflow/tensorflow/issues/40183).

### Left To Do ###

For frontend:

1. Display which model user chose in frontend

2. Add some logic in frontend, like first choose model and then upload image

3. Dsiplay result on a table with Top 5 accuracy

For backend:

1. Try with Pruning if possible

2. Documentation and code clean up

## Week2 ##

### Frontend ###

Achieve 3 points about left to do in previous section. Now frontend will display which model is chosen, and also results are available in a table with top 5 accuracy, as shown below.

![frontend](images/frontend/frontend_2.png)

### Backend ###

Apply pruning on MobileNet and retrain on imagenet2012 dataset. And the idea of pruning is trying to push network weights to be sparse / zero, which will decrease the size of the model. 

### Result ###

We evaluate original mobilenet and pruned mobilenet on 800000 images from imagenet train (66%) and 50000 images from validation dataset (100%):

| model | accuracy/train| used time/train | accuracy/validation| used time/validation | compressed size | 
| -----:|------:| -----:|-----:|-----:|-----:|
| Original MobileNet  | 0.8711 | 3043 s | 0.6917 |228 s| 15471 KB|
| Pruned MobileNet   |  0.8781 | 2711 s | 0.6733 | 204 s| 8807 KB|

So after pruning, the time used to run evaluation slightly decreases, accuracy on validation set drops a bit. Interesting to see that the compressed size becomes hafl smaller after pruning, which matches with our pruning goal (initial sparsity is 50%). Moreover, this indicates that it is possible to have a 8x smaller model if combining pruning and quantization. 

## Summary ##

### Why chosen this solution ###

The reason I chose speeding up forward pass is that I feel this one is more fun and more related to my previous experience. And I chose to build all things from scratch in frontend is because I want to learn some basic about web development. And reason setting up Flask backend instead of using tensorflow-js is that I do not want to convert every model I developed and convert in .js, which takes time to get feedback on the model performance. But of course, the drawback of this approach is that it requires more time to think and develop.

### Obstacles ###

1. whole web design is new
   
2. preprocessing method is different from model to model

3. quantize to int models are tricky when prepare representative dataset

4. download imagenets and run with such big dataset

### Future Step ###

1. More advanced and better tuning during the pruning, which could preserve or even improve model performances

2. A better structure in the frontend

3. Try with Tensorflow-model-server

### To Be Notice ###

if want to run `/src/tools/quantize_model.py` or `/src/tools/pruning.py`

1. replace `/src/tools/schema_py_generated.py` under your python virtualenv `site-packages/tensorflow/lite/python`

2. download imagenet 2012 dataset manually from [imagenet](http://www.image-net.org/challenges/LSVRC/2012/downloads) and place under `~/tensorflow_datasets/downloads/manual/`

