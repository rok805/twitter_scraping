## 트위터 데이터 수집 크롤러

### 특정 단어를 포함하고 있는 트위터 데이터를 수집합니다.
#### 원하는 특정 단어를 설정하고, 이와 관련된 데이터를 수집할 수 있습니다. 


 데이터 수집을 위해서 트위터에 접근을 하는데, 제한사항이 많다. 시간적으로도 양적으로도 트위터 자체적으로 데이터에 대한 소유권을 그렇게 주장한다. 
 하지만 아래에 링크처럼 그러한 제한없이 크롤러를 만드시는 분들이 있어서 참고하여 잘 사용했다.

twitterscraper 라는 패키지를 설치해야한다. 늘 그렇듯 터미널에 pip install twitterscraper 하면 된다.

 아래의 코드는 한달치를 수집하고 데이터프레임에 넣어서 곧바로 엑셀로 내보내는 것이라서 다소 복잡해보일 수도 있지만 단 하나의 코드 query_tweets만 보면 된다. 이 함수 안에 원하는 키워드(여기서는 bitcoin) 그리고 limit(여기서는 100000)을 지정하고, begindate, enddate 를 아래 코드처럼 형식에 맞게끔만 넣어주면 된다.
