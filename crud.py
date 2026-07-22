from bson import ObjectId
from database import sales_collection

def add_sale(date, salesperson, region, category, product, quantity, unit_price):
    """
    Add a new sales record to the MongoDB database.

    Args:
        date (str): Date of the sale (YYYY-MM-DD).
        salesperson (str): Name of the salesperson.
        region (str): Sales region.
        category (str): Product category.
        product (str): Product name.
        quantity (int): Number of units sold.
        unit_price (float): Price per unit.

    Returns:
        ObjectId: The ID of the inserted document.
    """

    # Calculate total sales
    sales = quantity * unit_price

    sale = {
        "Date": date,
        "SalesPerson": salesperson,
        "Region": region,
        "Category": category,
        "Product": product,
        "Quantity": quantity,
        "UnitPrice": unit_price,
        "Sales": sales
    }

    result = sales_collection.insert_one(sale)

    return result.inserted_id

def update_sale(
    sale_id,
    new_date,
    new_salesperson,
    new_region,
    new_category,
    new_product,
    new_quantity,
    new_unit_price
):
    """
    Update an existing sales record using its MongoDB document ID.
    """

    new_sales = new_quantity * new_unit_price

    result = sales_collection.update_one(
        {"_id": ObjectId(sale_id)},
        {
            "$set": {
                "Date": new_date,
                "SalesPerson": new_salesperson,
                "Region": new_region,
                "Category": new_category,
                "Product": new_product,
                "Quantity": new_quantity,
                "UnitPrice": new_unit_price,
                "Sales": new_sales
            }
        }
    )

    return result