from download_tweets_from_search import get_all_tweets
import matplotlib.pyplot as plt
import get_sentimeant
import joystick as jk
import preprocessing
import pandas as pd
import datetime
import time

step_size = 60 #how often graph is updated (in seconds)
num_iterations = 30 #how long you want the graph to be

x=[]
lib=[]
rep=[]
k = 0
for i in range(num_iterations):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    get_all_tweets("place:5635c19c2b5078d1 (coronavirus)",timestamp)
    print("Saved tweets for",timestamp)
    tweets = pd.read_csv("covid-19_"+timestamp+"_tweets.csv")
    tweets = tweets["text"]

    all_tweets = " ".join(tweets)
    all_tweets = preprocessing.clean_str(all_tweets)
    sentences = preprocessing.sequence_text(all_tweets)
    print("Preprocessed tweets")

    #get emotion - CHANGE THIS FOR POLITICAL OR TOXICITY
    emos = get_sentimeant.emotion(sentences)
    sadness = emos[0]
    fear =  emos[1]

    x.append(i)
    k+=1
    lib.append(sadness)
    rep.append(fear)
    time.sleep(step_size)

plt.plot(x, lib, 'blue', x, rep, 'red')
plt.plot(sadness,fear)
plt.show()
