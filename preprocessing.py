from nltk.corpus import stopwords, wordnet
from nltk import download
import tensorflow as tf
from io import open
import numpy as np
import json
import re


#Get rid of noise from dataset
def clean_str(string):
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`\.]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)

    word_list = string.split(' ')
    # string = ""
    # for word in word_list:
    #     if word not in stopwords.words('english'):
    #         if wordnet.synsets(word):
    #             string = string + word + " "
    return string.strip().lower()

#For turning long text into sentences to put into each model
def sequence_text (text, max_len=50):
    word_list = text.split(' ')
    filtered_word_list = word_list[:]
    for word in word_list:
        if word in stopwords.words('english'):
            filtered_word_list.remove(word)
    word_list = filtered_word_list
    sentences = []
    i = 0
    while i < len(word_list):
        k = 0
        sentence = ""
        while k < max_len:
            if k+i >= len(word_list):
                pass
            else:
                sentence=sentence+word_list[i+k]+" "
            k+=1
        sentences.append(sentence)
        i+=max_len

    return sentences

#Gets tokenizer from json
def tokenizer_from_json(json_string):
    """Parses a JSON tokenizer configuration file and returns a
    tokenizer instance.
    # Arguments
        json_string: JSON string encoding a tokenizer configuration.
    # Returns
        A Keras Tokenizer instance
    """
    tokenizer_config = json.loads(json_string)
    config = tokenizer_config.get('config')

    word_counts = json.loads(config.pop('word_counts'))
    word_docs = json.loads(config.pop('word_docs'))
    index_docs = json.loads(config.pop('index_docs'))
    # Integer indexing gets converted to strings with json.dumps()
    index_docs = {int(k): v for k, v in index_docs.items()}
    index_word = json.loads(config.pop('index_word'))
    index_word = {int(k): v for k, v in index_word.items()}
    word_index = json.loads(config.pop('word_index'))

    tokenizer = tf.keras.preprocessing.text.Tokenizer(**config)
    tokenizer.word_counts = word_counts
    tokenizer.word_docs = word_docs
    tokenizer.index_docs = index_docs
    tokenizer.word_index = word_index
    tokenizer.index_word = index_word

    return tokenizer
