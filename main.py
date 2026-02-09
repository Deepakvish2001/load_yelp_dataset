from read_json import business_df
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