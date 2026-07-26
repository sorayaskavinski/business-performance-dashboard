from database.crud import delete_sale
from features.search_sales import select_sale

def run_delete_sale():
    print("\nDelete a Sale Record\n")
    from features.search_sales import select_sale

    sale_id = select_sale()

    if sale_id is None:
        return

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete the sale with ID {sale_id}? (y/n): ")
    if confirm.lower() != 'y':
        print("Deletion cancelled.")
        return

    # Delete the sale record
    deleted_count = delete_sale(sale_id)

    if deleted_count > 0:
        print(f"\nSale with ID {sale_id} has been deleted successfully.")
    else:
        print(f"\nNo sale found with ID {sale_id}.")