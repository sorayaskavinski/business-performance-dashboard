from database.database import sales_collection
from bson import ObjectId
from database.crud import update_sale
from features.search_sales import select_sale

def run_update_sale():
    print("\nEnter the sale information to update:\n")

    from features.search_sales import select_sale

    sale_id = select_sale()

    if sale_id is None:
        return

    # Fetch the existing sale record
    existing_sale = sales_collection.find_one({"_id": ObjectId(sale_id)})

    if not existing_sale:
        print("Sale record not found.")
        return

    print("\nExisting Sale Record:")
    print("\nCurrent Sale Information")
    print("-" * 40)

    print(f"Date: {existing_sale['Date']}")
    print(f"Sales Person: {existing_sale['SalesPerson']}")
    print(f"Region: {existing_sale['Region']}")
    print(f"Category: {existing_sale['Category']}")
    print(f"Product: {existing_sale['Product']}")
    print(f"Quantity: {existing_sale['Quantity']}")
    print(f"Unit Price: ${existing_sale['UnitPrice']:.2f}")
    print(f"Sales: ${existing_sale['Sales']:.2f}")

    print("-" * 40)

    # Prompt for new values (press Enter to keep existing values)
    date = input(f"Date (YYYY-MM-DD) [{existing_sale['Date']}]: ") or existing_sale['Date']
    salesperson = input(f"Sales Person [{existing_sale['SalesPerson']}]: ") or existing_sale['SalesPerson']
    region = input(f"Region [{existing_sale['Region']}]: ") or existing_sale['Region']
    category = input(f"Category [{existing_sale['Category']}]: ") or existing_sale['Category']
    product = input(f"Product [{existing_sale['Product']}]: ") or existing_sale['Product']

    quantity_input = input(f"Quantity [{existing_sale['Quantity']}]: ")
    quantity = int(quantity_input) if quantity_input else existing_sale['Quantity']

    unit_price_input = input(f"Unit Price [{existing_sale['UnitPrice']}]: ")
    unit_price = float(unit_price_input) if unit_price_input else existing_sale['UnitPrice']

    # Update the sale record
    updated_id = update_sale(
        sale_id,
        date,
        salesperson,
        region,
        category,
        product,
        quantity,
        unit_price
    )

    print("\nSale updated successfully!")
    print(f"Document ID: {updated_id}")

