from dashboard import run_dashboard
from features.add_sales import run_add_sale
from features.update_sales import run_update_sale
from features.delete_sales import run_delete_sale
from features.search_sales import search_dashboard


def menu():

    while True:

        print("\n" + "=" * 50)
        print(" BUSINESS PERFORMANCE DASHBOARD")
        print("=" * 50)

        print("1. Dashboard")
        print("2. Add Sale")
        print("3. Search Sales")
        print("4. Update Sale")
        print("5. Delete Sale")
        print("6. Exit")

        option = input("Option: ")

        if option == "1":
            run_dashboard()

        elif option == "2":
            run_add_sale()

        elif option == "3":
            search_dashboard()

        elif option == "4":
            run_update_sale()

        elif option == "5":
            run_delete_sale()

        elif option == "6":
            break

if __name__ == "__main__":
    menu()
