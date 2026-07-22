from dashboard import (
    load_data_from_mongodb,
    clean_data,
    display_dataset_info,
    display_summary,
    sales_by_category,
    sales_by_month,
    create_category_chart,
    create_monthly_chart,
)

from crud import add_sale

def run_dashboard():

    sales_df = load_data_from_mongodb()

    sales_df = clean_data(sales_df)

    display_dataset_info(sales_df)

    display_summary(sales_df)

    sales_by_category(sales_df)

    sales_by_month(sales_df)

    create_category_chart(sales_df)

    create_monthly_chart(sales_df)

    print("\nAnalysis completed Successfully.")

def menu():

    while True:

        print("\n" + "=" * 50)
        print(" BUSINESS PERFORMANCE DASHBOARD")
        print("=" * 50)

        print("1. View Dashboard")
        print("2. Add Sale")
        print("3. Update Sale")
        print("4. Delete Sale")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            run_dashboard()

        elif choice == "2":

            print("\nEnter the sale information:\n")

            date = input("Date (YYYY-MM-DD): ")
            salesperson = input("Sales Person: ")
            region = input("Region: ")
            category = input("Category: ")
            product = input("Product: ")

            quantity = int(input("Quantity: "))
            unit_price = float(input("Unit Price: "))

            sale_id = add_sale(
                date,
                salesperson,
                region,
                category,
                product,
                quantity,
                unit_price,
            )

            print("\nSale added successfully!")
            print(f"Document ID: {sale_id}")

        elif choice == "3":
            print("Update Sale")

        elif choice == "4":
            print("Delete Sale")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
