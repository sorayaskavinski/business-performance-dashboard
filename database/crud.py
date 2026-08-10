from bson import ObjectId
from database.database import sales_collection

def get_all_sales():
    """
    Retrieve all sales records from MongoDB.
    """
    return list(sales_collection.find())

def add_sale(
    date,
    salesperson,
    region,
    category,
    product,
    quantity,
    unit_price
):

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

def search_sales(product="", category="", salesperson="", region="", date=""):
    """
    Search sales dynamically using multiple optional fields.
    Ignores empty/blank filters so users can combine any number of criteria.
    """
    query = {}

    # Adiciona à busca apenas os campos que realmente contêm algum texto
    if product and product.strip():
        query["Product"] = {"$regex": product.strip(), "$options": "i"}
        
    if category and category.strip():
        query["Category"] = {"$regex": category.strip(), "$options": "i"}
        
    if salesperson and salesperson.strip():
        query["SalesPerson"] = {"$regex": salesperson.strip(), "$options": "i"}
        
    if region and region.strip():
        query["Region"] = {"$regex": region.strip(), "$options": "i"}
        
    if date and date.strip():
        query["Date"] = {"$regex": date.strip(), "$options": "i"}

    # If you dont find any query, return all sales records
    if not query:
        return list(sales_collection.find())

    return list(sales_collection.find(query))

def update_sale(
    sale_id,
    new_date,
    new_salesperson,
    new_region,
    new_category,
    new_product,
    new_quantity,
    new_unit_price,
):
    """
    Update an existing sales record using its MongoDB document ID.
    """

    try:
        object_id = ObjectId(sale_id)
    except Exception:
        return None

    new_sales = new_quantity * new_unit_price

    result = sales_collection.update_one(
        {"_id": object_id},
        {
            "$set": {
                "Date": new_date,
                "SalesPerson": new_salesperson,
                "Region": new_region,
                "Category": new_category,
                "Product": new_product,
                "Quantity": new_quantity,
                "UnitPrice": new_unit_price,
                "Sales": new_sales,
            }
        },
    )

    return result

def delete_sale(sale_id):
    """
    Delete a sales record using its MongoDB document ID.
    """

    try:
        object_id = ObjectId(sale_id)
    except Exception:
        return None

    result = sales_collection.delete_one({"_id": object_id})

    return result.deleted_count

def get_products():
    return sorted(sales_collection.distinct("Product"))


def get_categories():
    return sorted(sales_collection.distinct("Category"))


def get_regions():
    return sorted(sales_collection.distinct("Region"))


def get_salespeople():
    return sorted(sales_collection.distinct("SalesPerson"))

