from read_json import business_df
from read_json import checkin_df
from read_json import tip_df
from read_json import review_df
from read_json import user_df
from db_connect import engine

def load_dataframe(df, table_name):
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='replace',
        index=False
    )
    print(f"{table_name} uploaded successfully 🚀")

load_dataframe(business_df, 'business')
print("done successfully")

load_dataframe(checkin_df, 'checkin')
print("done successfully")

load_dataframe(tip_df, 'tip')
print("done successfully")

load_dataframe(review_df, 'review')
print("done successfully")

load_dataframe(user_df, 'user')
print("done successfully")