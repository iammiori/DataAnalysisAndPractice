# DataAnalysisAndPractice
> This project is  **Sejong Univ. 19-Fall Data Analysis And Practice class final project**.

> team member : Sohyeon Kwon, Miyeon Lee


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
  <br> ex) <br>![image](https://user-images.githubusercontent.com/46439995/70145217-ec3c0d80-16e2-11ea-9aef-37b5f01e0abd.png)


### Library Dependencies
- Python 3.7.3
- pandas, numpy
- json,csv
- surprise



### Directory
![image](https://user-images.githubusercontent.com/46439995/70844467-c8b45800-1e84-11ea-879b-38ead74872f1.png)




### Procedure
1. install all the dependencies
2. unzip .tar (you can get json file)
<br> how to ) cmd : `tar xvf your_path.tar`



### Component
**1. preprocessing**
- calldataset > call_dataset.py
  - def json_2_csv : `invert json file to csv file`
  - def review : `load review data based on the user with the most acitve`
  - def stroe : `To map the store ID and name, we load the store list from business.json and removed the duplicates `
  - def rating : `final review file`
  - def change_column : `change column`
  - def save_npy : `make matrix and save it using numpy`
  <br>
**2. similarity**
- similarity > cal_similarity.py
  - def cos : `Cosine similarity`
  - def PCC : `Pearson Correlation Coefficient similarity`
  - def Jac : `Jaccard measure similarity`
<br>

**3. memor based cf**

<br>

**4. surprise**
- you can get result with csv file.
- Input the files and algorithms to be stored as parameters.
- ex)<br>
![image](https://user-images.githubusercontent.com/46439995/70629768-d8a61f00-1c6d-11ea-8ea3-a0a28557125d.png)


1. compare algorithm <br><br>
![image](https://user-images.githubusercontent.com/46439995/70629672-b2807f00-1c6d-11ea-86c1-127b7bdd91c4.png)

2. SVD result <br><br>
![image](https://user-images.githubusercontent.com/46439995/70629737-c926d600-1c6d-11ea-89bd-6f40a72efc6c.png)
<br>

3. NDCG
- 예측 rating 값을 뽑아내는 함수 출력이 길기 때문에 이를 csv,npy로 저장하는 코드를 포함
- 이를 불러와, 따로 측정한 결과
![image](https://user-images.githubusercontent.com/46439995/70643950-50cc0f00-1c85-11ea-8b7c-2dc71d9e98f3.png)

  
  
  
  
  
### To Run
- run `basic_test.py`  
