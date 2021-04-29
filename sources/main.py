from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
import time

for i in range(1,30,1):
    result = pd.DataFrame(columns=['text','time'])
    if __name__ == '__main__':

        tmp1=[]
        tmp2=[]
        start=time.time()
        
        for tweet in query_tweets('bitcoin',100000, begindate=dt.date(2019,9,i), enddate=dt.date(2019,9,i+1)):
            

        # print(tweet.timestamp) #작성시간
        # print(tweet.text)      #트윗내용
            tmp1.append(tweet.text)
            tmp2.append(tweet.timestamp)

        result['text'] = tmp1
        result['time'] = tmp2
        result.to_excel('bitcoin_2019_9_{}.xlsx'.format(i))
        del result
        print(i)
        print(time.time()-start)
