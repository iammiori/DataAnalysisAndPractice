import json,csv
import os
import pandas as pd

class JsonCsvConverter(object):
    
    # user 중 yelp를 많이 사용한 user 부르는 함수
    headers = True    
    def json_2_csv(self, json_file, csv_file):
        
        global headers 
        headers = True 
        with open(json_file,encoding='utf-8') as jsonf, open(csv_file,"w",encoding="utf-8") as csvf:
            for line in jsonf:
                data = json.loads(line)
                # 필요 없는 key 값 삭제, 시간 효율적
                #data.pop("review_count")
                data.pop("yelping_since")
                data.pop("friends")
                data.pop("useful")
                data.pop("funny")
                data.pop("cool")
                data.pop("fans")
                data.pop("elite")
                data.pop("average_stars")
                data.pop("compliment_hot")
                data.pop("compliment_more")
                data.pop("compliment_profile")
                data.pop("compliment_cute")
                data.pop("compliment_list")
                data.pop("compliment_note")
                data.pop("compliment_plain")
                data.pop("compliment_cool")
                data.pop("compliment_funny")
                data.pop("compliment_writer")
                data.pop("compliment_photos")


                if headers:
                    keys = []
                    for k,v in data.items():
                        keys.append(k)
                    writer = csv.DictWriter(csvf,fieldnames=keys)
                    writer.writeheader()
                    headers = False
                if data['review_count']>=1457:
                    # user top 500보기 위해 1457 에서 컷
                    writer.writerow(data)
                    
    # review 를 불러오는 함수 (많이 사용한 user를 기반으로)
    def review(self,json_file,csv_file,user_file):
        
        # user_id 와 name matching 을 위해 서로 list에 저장
        # - list에 각각 저장하여 서로 index로 통해 mapping 할 계획이다
        # - user_id_list : user의 id
        # - user_name_list : user의 name
        #-----------------------
        user_df = pd.read_csv(user_file)
        user_id_list = []
        for i in range(0,len(user_df)):
            tmp = user_df["user_id"].iloc[i]
            user_id_list.append(tmp)
        print(len(user_id_list))

        user_name_list = []
        for i in range(0,len(user_df)):
            tmp = user_df["name"].iloc[i]
            user_name_list.append(tmp)
        print(len(user_name_list))

        global headers
        headers = True
        with open(json_file,encoding='utf-8') as jsonf, open(csv_file,"w",encoding="utf-8") as csvf:
            for line in jsonf:
                data = json.loads(line)
                data.pop("review_id")
                data.pop("date")
                data.pop("text")
                data.pop("useful")
                data.pop("funny")
                data.pop("cool")

                if headers:
                    keys = []
                    for k,v in data.items():
                        # key 값은 column 으로 value는 값으로 저장
                        keys.append(k)
                    writer = csv.DictWriter(csvf,fieldnames=keys)
                    writer.writeheader()
                    headers = False

                if data["user_id"] in user_id_list:
                    index_num = user_id_list.index(data["user_id"])
                    data["user_id"] = user_name_list[index_num]
                    writer.writerow(data)

    # 가게명을 바꾸기 위해 가게 목록을 불러오고, 중복을 제거할것
    def store(self,json_file,csv_file,review_file):
        
        # list 에 저장
        review_df = pd.read_csv(review_file)
        store_id_list = []
        for i in range(len(review_df)):
            tmp = review_df["business_id"].iloc[i]
            store_id_list.append(tmp)
        print(len(store_id_list))
        store_id_list_clean = list(set(store_id_list))
        print(len(store_id_list_clean)) 
        
        # 중복 제거 완료
        
        global headers
        headers = True
        with open(json_file,encoding='utf-8') as jsonf, open(csv_file,"w",encoding="utf-8") as csvf:
            for line in jsonf:
                data = json.loads(line)
                #print(data)
                data.pop("address")
                data.pop("city")
                data.pop("state")
                data.pop("postal_code")
                #data.pop("review_count")
                data.pop("latitude")
                data.pop("longitude")
                data.pop("stars")
                data.pop("is_open")
                data.pop("attributes")
                data.pop("categories")
                data.pop("hours")


                if headers:
                    keys = []
                    # k : key 값 v : value 값
                    for k,v in data.items():
                        #print("{} {} ".format(k,v))
                        keys.append(k)
                    writer = csv.DictWriter(csvf,fieldnames=keys)
                    # column 을 key값으로
                    writer.writeheader()
                    headers = False

                if data["business_id"] in store_id_list_clean:
                    writer.writerow(data)
                    
                    
    # 최종 review 파일 
    def rating(self,json_file,csv_file,user_file,business_file):

        user_df = pd.read_csv(user_file)
        user_id_list = []
        for i in range(0,len(user_df)):
            tmp = user_df["user_id"].iloc[i]
            user_id_list.append(tmp)
        print(len(user_id_list))

        user_name_list = []
        for i in range(0,len(user_df)):
            tmp = user_df["name"].iloc[i]
            user_name_list.append(tmp)
        print(len(user_name_list))
        
        # list에 저장
        business_df = pd.read_csv(business_file)
        store_name_list = []
        for i in range(len(business_df)):
            tmp = business_df["name"].iloc[i]
            store_name_list.append(tmp)
        print(len(store_name_list))  

        store_id_list2 = []
        for i in range(len(business_df)):
            tmp = business_df["business_id"].iloc[i]
            store_id_list2.append(tmp)
        print(len(store_id_list2))        

        global headers
        headers = True
        with open(json_file,encoding='utf-8') as jsonf, open(csv_file,"w",encoding="utf-8") as csvf:    
            for line in jsonf:
                data = json.loads(line)
                # 필요없는 key값삭제하면서 나중에 읽어올때, 시간 절약
                data.pop("review_id")
                data.pop("date")
                data.pop("text")
                data.pop("useful")
                data.pop("funny")
                data.pop("cool")


                if headers:
                    keys = []
                    for k,v in data.items():
                        # key 값은 column 으로 value 는 값으로 저장
                        keys.append(k)
                    writer = csv.DictWriter(csvf,fieldnames=keys)
                    writer.writeheader()
                    headers = False

                # 많은 user 중 많이 rating 한 user 만 갖고오고    
                if data["user_id"] in user_id_list:

                    # user_id 는 이름으로 바꿔라 (바이트수 절약위해)
                    index_num = user_id_list.index(data["user_id"])
                    data["user_id"] = user_name_list[index_num]

                    # 마찬가지로 business_id 도 상점이름으로 바꿔라
                    index_num2 = store_id_list2.index(data["business_id"])
                    data["business_id"] = store_name_list[index_num2]
                    writer.writerow(data)

                    
                    
                    
    def change_column(self,file):
        review_df = pd.read_csv(file)
        review_df = review_df.rename(columns={'user_id':'user','business_id':'store'})
        review_df.to_csv(file,index=False)              
                    
'''       
if __name__ == '__main__':
    converter = JsonCsvConverter()
    #converter.csv_2_json("./csv_user_info.csv", "./json_user_info.json")
    converter.review("../dataset/review.json", "../dataset/review.csv")
    #converter.json_2_csv("../dataset/user.json", "../dataset/user.csv")
'''