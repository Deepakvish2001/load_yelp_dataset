import pandas as pd
import json

file_path_business = r'C:\YELP Project\yelp_dataset\yelp_academic_dataset_business.json'

with open(file_path_business,'r', encoding='utf-8') as f:
    business_data = [json.loads(line) for line in f]
business_df = pd.DataFrame(business_data)
print("json file loaded")
business_df.drop(['attributes','hours'], axis=1, inplace=True)