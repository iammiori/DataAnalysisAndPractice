from calldata import call_dataset
import numpy as np

# user json to csv
converter = call_dataset.JsonCsvConverter()
converter.json_2_csv("./dataset/user.json", "./dataset/user.csv")

