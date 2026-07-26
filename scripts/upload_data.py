import pandas as pd
from database.database import sales_collection

df = pd.read_csv("data/sales_data.csv")

records = df.to_dict("records")

sales_collection.insert_many(records)

print("Data uploaded successfully!")