import json,csv
import os

class JsonCsvConverter(object):
    headers = True    
    def json_2_csv(self, json_file, csv_file):
        
        global headers 
        headers = True 
        with open(json_file,encoding='utf-8') as jsonf, open(csv_file,"w",encoding="utf-8") as csvf:
            for line in jsonf:
                data = json.loads(line)
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


       
'''            
if __name__ == '__main__':
    converter = JsonCsvConverter()
    #converter.csv_2_json("./csv_user_info.csv", "./json_user_info.json")
    #converter.csv_2_json_by_dictreader("./csv_user_info.csv", "./json_user_info.json")
    converter.json_2_csv("../dataset/user.json", "../dataset/user.csv")
'''