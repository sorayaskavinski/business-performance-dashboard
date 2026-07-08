"""
generate_data.py

Creates a fictional business sales dataset for the
Business Performance Dashboard project.

Author: Soraya Skavinski
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

# -----------------------------
# Configuration
# -----------------------------

NUMBER_OF_RECORDS = 1000

products = [
    ("Laptop", "Electronics", 1200),
    ("Monitor", "Electronics", 300),
    ("Keyboard", "Electronics", 50),
    ("Mouse", "Electronics", 35),
    ("Printer", "Electronics", 250),
    ("Desk", "Furniture", 450),
    ("Office Chair", "Furniture", 220),
    ("Bookshelf", "Furniture", 180),
    ("Notebook", "Office Supplies", 8),
    ("Pen Pack", "Office Supplies", 12),
    ("Paper", "Office Supplies", 15),
    ("Calculator", "Office Supplies", 40),
]

regions = [
    "North",
    "South",
    "East",
    "West"
]

sales_people = [
    "Alice",
    "Brian",
    "Carlos",
    "Diana",
    "Emily",
    "Frank",
    "Grace",
    "Henry"
]

# -----------------------------
# Create data folder
# -----------------------------

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

csv_file = data_folder / "sales_data.csv"

# -----------------------------
# Generate random sales
# -----------------------------

start_date = datetime(2025, 1, 1)

with open(csv_file, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Date",
        "SalesPerson",
        "Region",
        "Category",
        "Product",
        "Quantity",
        "UnitPrice",
        "Sales"
    ])

    for _ in range(NUMBER_OF_RECORDS):

        random_days = random.randint(0, 364)
        sale_date = start_date + timedelta(days=random_days)

        product, category, price = random.choice(products)

        quantity = random.randint(1, 10)

        sales = quantity * price

        writer.writerow([
            sale_date.strftime("%Y-%m-%d"),
            random.choice(sales_people),
            random.choice(regions),
            category,
            product,
            quantity,
            price,
            sales
        ])

print("======================================")
print("Dataset created successfully!")
print(f"Records generated: {NUMBER_OF_RECORDS}")
print(f"File saved to: {csv_file}")
print("======================================")