from database.crud import add_sale

def run_add_sale():

    print("\nEnter the sale information:\n")

    date = input("Date (YYYY-MM-DD): ")
    salesperson = input("Sales Person: ")
    region = input("Region: ")
    category = input("Category: ")
    product = input("Product: ")

    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            unit_price = float(input("Unit Price: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    sale_id = add_sale(
        date,
        salesperson,
        region,
        category,
        product,
        quantity,
        unit_price
    )

    print("\nSale added successfully!")
    print(f"Document ID: {sale_id}")