from calldata import call_dataset
from similarity import cal_similarity
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

# ui matrix matrix로
converter.save_npy("./dataset/rating_final.csv","./dataset/real_matrix")

# calculate similarity
# 1. cos
calsim = cal_similarity.CalculSim()

calsim.cos("./dataset/real_matrix.npy")

calsim.PCC("./dataset/real_matrix.npy")

calsim.Jac("./dataset/real_matrix.npy")