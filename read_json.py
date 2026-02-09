import pandas as pd
import json

file_path_business = r'C:\YELP Project\yelp_dataset\yelp_academic_dataset_business.json'
file_path_checkin = r'C:\YELP Project\yelp_dataset\yelp_academic_dataset_checkin.json'
file_path_tip = r'C:\YELP Project\yelp_dataset\yelp_academic_dataset_tip.json'

with open(file_path_business,'r', encoding='utf-8') as f:
    business_data = [json.loads(line) for line in f]
business_df = pd.DataFrame(business_data)
print("json file loaded")
business_df.drop(['attributes','hours'], axis=1, inplace=True)

with open(file_path_checkin,'r', encoding='utf-8') as f:
    checkin_data = [json.loads(line) for line in f]
checkin_df = pd.DataFrame(checkin_data)
print("json file loaded")

with open(file_path_tip,'r', encoding='utf-8') as f:
    tip_data = [json.loads(line) for line in f]
tip_df = pd.DataFrame(tip_data)
print("json file loaded")



