from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)

db = client["business_dashboard"]

sales_collection = db["sales"]


def get_sales():
    """
    Retrieve all sales records from MongoDB.
    """
    records = list(sales_collection.find())

    for record in records:
        record.pop("_id", None)

    return records
