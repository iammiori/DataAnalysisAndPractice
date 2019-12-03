# DataAnalysisAndPractice
> This project is  **Sejong Univ. 19-Fall Data Analysis And Practice class final project**.
## Recommender system using yelp

### Overview

- data : yelp (round 13) <br>
**data size is too big to load, so you should download the yelp data [here](https://www.yelp.com/dataset) and, put in the dataset folder**
- dataset 
  - user.json ( You can get it by downloading yelp )
  - business.json ( You can get it by downloading yelp )
  - review.json ( You can get it by downloading yelp )
  - user.csv ( You can get it by running the code )
  - review.csv ( You can get it by running the code )
  - business_clean.csv ( You can get it by running the code )  
  **- rating_final.csv ( You can get it by running the code )** **=> We'll use this data**  
  <br>
> similarity, memory-based CF, surprise 를 위해 가공된 데이터는 제공했다 (rating_final.csv , real_matrix.npy ) <br>
  따라서 코드를 돌릴 때 json을 csv로 바꾸는 코드는 주석처리가 필요하다

### Library Dependencies
- Python 3.7.3
- pandas, numpy
- json,csv
- surprise



### Procedure
1. install all the dependencies
2. unzip .tar (you can get json file)
<br> how to ) cmd : `tar xvf your_path.tar`



### Component
**1. preprocessing**
- calldataset > call_dataset.py
  - def json_2_csv : `invert json file to csv file`
  - def review : `많이 사용한 user를 기반으로 review data 불러오기`
  - def stroe : `가게명을 바꾸기 위한 가게 목록을 불러오고 중복 제거`
  - def rating : `최종 review 파일`
  - def change_column : `column 바꿔줌`
  - def save_npy : `matrix로 생성후 저장`
  
  
  
### To Run
- run `basic_test.py`  
