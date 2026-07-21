from database import sales_collection

records = list(sales_collection.find())

print(f"Number of records: {len(records)}")

print(records[0])