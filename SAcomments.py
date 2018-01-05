
from snownlp import SnowNLP,sentiment
import pandas as pd
import pylab as pl

def sentiment_analysis(infile):
    sentiments_list = []
    fin = open(infile,'r',encoding='utf-8')
    comments_list = fin.readlines()
    fin.close()
    for i in range(len(comments_list)-1):
        s=SnowNLP(comments_list[i].strip())
        sentiments_list.append(s.sentiments)
    return sentiments_list

def display_sentiments(infile):
    sentiments_list = sentiment_analysis(infile)
    x=range(len(sentiments_list))
    pl.plot(x,sentiments_list,'b.')
    pl.xlabel('sample')
    pl.ylabel('score')
    pl.show()

def selfTrainSentiment(infile):
    sentiment.train("pos","neg")
    sentiment.save('sentfwhyj.marshal')
    sentiments_list = sentiment_analysis(infile)
    x=range(len(sentiments_list))
    pl.plot(x,sentiments_list,'b.')
    pl.xlabel('sample')
    pl.ylabel('score')
    pl.show()

if __name__ == '__main__':
    #display_sentiments('origin_data')
    selfTrainSentiment('origin_data')
    #sentiment_list= sentiment_analysis('origin_data')
    #print (sentiment_list)
    #print (float(sum(sentiment_list)/len(sentiment_list)))