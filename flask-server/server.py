from flask import Flask, jsonify, request, render_template
from flask import flash, url_for, redirect, session

import pandas as pd
import numpy as np
import os 
import re

import tensorflow as tf
from numpy import array


from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.models import load_model 
from keras.utils.data_utils import pad_sequences

IMAGE_FOLDER = os.path.join('static','img_pool')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching

def init():
    global model, graph
    #load pretrained model
    model = tf.keras.models.load_model('../sentiment_analysis_model_new.h5')
    graph = tf.compat.v1.get_default_graph()

#for sentiment analysis
@app.route('/', methods = ['POST','GET'])
def home():
    return render_template('index.html')

@app.route('/sentiment_prediction', methods = ['POST'])
def sentiment():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = ''
        max_review_length = 500
        word_to_id = imdb.get_word_index()
        
        strip_special_chars = re.compile("[^A-Za-z0-9 ]+")
        text = text.lower().replace("<br />", " ")
        text = re.sub(strip_special_chars, "", text.lower())

        words = text.split()
        x_test = [[word_to_id[word] if (word in word_to_id and word_to_id[word]<=20000) else 0 for word in words]]
        x_test = pad_sequences(x_test, maxlen=500) 

        vector = np.array([x_test.flatten()])
        with graph.as_default():
            model = tf.keras.models.load_model('../sentiment_analysis_model_new.h5')
            probability = model.predict(array([vector][0]))[0][0]
            class1 = np.argmax(probability,axis = -1)
            
        if probability >= 0.5:
            sentiment = 'Negative'
            img_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Sad_Emoji.png')
        else:
            sentiment = 'Positive'
            img_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Smiling_Emoji.png')
        return render_template('index.html', text=text, sentiment=sentiment, probability=probability, image=img_filename)
    
if __name__ == '__main__':
    init()
    app.run(port=5001,debug = True)