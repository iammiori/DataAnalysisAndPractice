from calldata import call_dataset
import numpy as np
import pandas as pd

# user json to csv
#---------------------
converter = call_dataset.JsonCsvConverter()
converter.json_2_csv("./dataset/user.json", "./dataset/user.csv")

# user.csv shape = (500,3)
# review json to csv
#---------------------
converter.review("./dataset/review.json", "./dataset/review.csv","./dataset/user.csv")

# business 정리
converter.store("./dataset/business.json", "./dataset/business_clean.csv","./dataset/review.csv")

# 최종 username - businessname mapping    
converter.rating("./dataset/review.json", "./dataset/rating_final.csv","./dataset/user.csv","./dataset/business_clean.csv")

# column 변경
converter.change_column("./dataset/rating_final.csv")                    