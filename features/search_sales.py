from database.crud import (
    search_by_product,
    search_by_category,
    search_by_salesperson,
    search_by_region,
)


def display_results(results):
    """
    Display the search results.
    """

    if not results:
        print("\nNo records found.")
        return

    print(f"\nFound {len(results)} record(s).\n")

    for sale in results:

        print("-" * 60)
        print(f"ID: {sale['_id']}")
        print(f"Date: {sale['Date']}")
        print(f"Sales Person: {sale['SalesPerson']}")
        print(f"Region: {sale['Region']}")
        print(f"Category: {sale['Category']}")
        print(f"Product: {sale['Product']}")
        print(f"Quantity: {sale['Quantity']}")
        print(f"Unit Price: ${sale['UnitPrice']:.2f}")
        print(f"Sales: ${sale['Sales']:.2f}")

    print("-" * 60)


def search_sales():
    """
    Search sales records and return the results.
    """

    print("\n" + "=" * 50)
    print("SEARCH SALES")
    print("=" * 50)

    print("1. Search by Product")
    print("2. Search by Category")
    print("3. Search by Sales Person")
    print("4. Search by Region")

    choice = input("\nChoose an option: ")

    if choice == "1":

        product = input("Product: ")
        return search_by_product(product)

    elif choice == "2":

        category = input("Category: ")
        return search_by_category(category)

    elif choice == "3":

        salesperson = input("Sales Person: ")
        return search_by_salesperson(salesperson)

    elif choice == "4":

        region = input("Region: ")
        return search_by_region(region)

    else:

        print("\nInvalid option.")
        return []


def search_dashboard():
    """
    Search and display results.
    Used from the Main Menu.
    """

    results = search_sales()

    display_results(results)


def select_sale():
    """
    Search for a sale and return its MongoDB ID.
    Used by Update and Delete.
    """

    results = search_sales()

    if not results:
        return None

    display_results(results)

    sale_id = input("\nEnter the Sale ID: ")

    return sale_id