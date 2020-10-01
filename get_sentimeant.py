from tensorflow.keras.models import load_model
import tensorflow as tf
import preprocessing
import numpy as np
import json

# def sentiment(tweets):
#
def emotion(sentences):
    emotion = load_model('models/feeling_model.h5')
    with open('models/emotokenizer.json') as f:
        data = json.load(f)
        emotion_tokenizer = preprocessing.tokenizer_from_json(data)
    emotion_tokenized = np.array(list(tf.keras.preprocessing.sequence.pad_sequences(emotion_tokenizer.texts_to_sequences(sentences), 50, padding='post', truncating='post')))
    f_score = emotion.predict(emotion_tokenized)
    return [f_score[0][4], f_score[0][1]]

def political(sentences):
    political_bias = load_model('models/political_bias.h5')
    with open('models/politicaltokenizer.json') as f:
        data = json.load(f)
        political_tokenizer = preprocessing.tokenizer_from_json(data)
    political_tokenized = np.array(list(tf.keras.preprocessing.sequence.pad_sequences(political_tokenizer.texts_to_sequences(sentences), 50, padding='post', truncating='post')))
    liberal = political_bias.predict(political_tokenized)[0][0]
    return liberal

def toxicity(sentences):
    toxic = load_model('models/toxicity.h5')
    with open('models/toxictokenizer.json') as f:
        data = json.load(f)
        toxic_tokenizer = preprocessing.tokenizer_from_json(data)
    toxic_tokenized = np.array(list(tf.keras.preprocessing.sequence.pad_sequences(toxic_tokenizer.texts_to_sequences(sentences), 50, padding='post', truncating='post')))
    toxicity = toxic.predict(toxic_tokenized)
    return toxicity
