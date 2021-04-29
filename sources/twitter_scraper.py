from twitterscraper import query_tweets
import pandas as pd
import datetime as dt
import time

result = pd.DataFrame(columns=['text','time'])
if __name__ == '__main__':

    tmp1=[]
    tmp2=[]
    start=time.time()

    for tweet in query_tweets('bitcoin',100000, begindate=dt.date(2019,9,30), enddate=dt.date(2019,10,1)):

#         print(tweet.timestamp) #작성시간
#        print(tweet.text)      #트윗내용
        tmp1.append(tweet.text)
        tmp2.append(tweet.timestamp)
    result['text'] = tmp1
    result['time'] = tmp2
    result.to_excel('bitcoin_2019_9_{}.xlsx'.format(30))
    del result
