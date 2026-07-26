from database.crud import (
    search_by_product,
    search_by_category,
    search_by_salesperson,
    search_by_region,
)


def display_results(results):
    """
    Display search results as a numbered list.
    """

    if not results:
        print("\nNo records found.")
        return

    print(f"\nFound {len(results)} record(s):\n")

    for index, sale in enumerate(results, start=1):

        print(
            f"{index}. "
            f"{sale['Product']} | "
            f"{sale['SalesPerson']} | "
            f"{sale['Region']} | "
            f"${sale['Sales']:.2f}"
        )

def display_sale(sale):

    print("\n" + "-" * 50)

    print(f"ID: {sale['_id']}")
    print(f"Date: {sale['Date']}")
    print(f"Sales Person: {sale['SalesPerson']}")
    print(f"Region: {sale['Region']}")
    print(f"Category: {sale['Category']}")
    print(f"Product: {sale['Product']}")
    print(f"Quantity: {sale['Quantity']}")
    print(f"Unit Price: ${sale['UnitPrice']:.2f}")
    print(f"Sales: ${sale['Sales']:.2f}")

    print("-" * 50)


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
    Search for a sale and let the user select it by number.
    """

    results = search_sales()

    if not results:
        return None

    display_results(results)

    while True:

        try:

            option = int(
                input(
                    f"\nChoose a sale (1-{len(results)}): "
                )
            )

            if 1 <= option <= len(results):

                selected_sale = results[option - 1]

                display_sale(selected_sale)

                confirm = input(
                    "\nUse this sale? (Y/N): "
                )

                if confirm.lower() == "y":
                    return str(selected_sale["_id"])

                else:
                    return None

            else:

                print("Invalid option.")

        except ValueError:

            print("Please enter a valid number.")


def choose_option(title, options):

    print(f"\n{title}")
    print("-" * 40)

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("\nChoose an option: "))

            if 1 <= choice <= len(options):
                return options[choice - 1]

            print("Invalid option.")

        except ValueError:
            print("Please enter a number.")