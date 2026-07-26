from bson import ObjectId
from database.database import sales_collection


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

def search_by_product(product):
    """
    Search sales by product name.
    """
    return list(
        sales_collection.find(
            {"Product": {"$regex": product, "$options": "i"}}
        )
    )


def search_by_category(category):
    """
    Search sales by category.
    """
    return list(
        sales_collection.find(
            {"Category": {"$regex": category, "$options": "i"}}
        )
    )


def search_by_salesperson(salesperson):
    """
    Search sales by salesperson.
    """
    return list(
        sales_collection.find(
            {"SalesPerson": {"$regex": salesperson, "$options": "i"}}
        )
    )


def search_by_region(region):
    """
    Search sales by region.
    """
    return list(
        sales_collection.find(
            {"Region": {"$regex": region, "$options": "i"}}
        )
    )



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