from django.shortcuts import render, redirect
from django.contrib import messages
from database.crud import (get_all_sales, search_sales as search_sales_db, delete_sale as delete_sale_db,
    update_sale as update_sale_db,sales_collection, add_sale as add_sale_db)
from bson import ObjectId
import pandas as pd


def home(request):
    """
    Display the application's home page.
    """

    return render(request, "home.html")

def get_all_sales_view(request):
    """
    View to retrieve and display all sales records.
    """
    sales = get_all_sales()
    for sale in sales:
        sale['id'] = str(sale['_id'])  # Convert ObjectId to string for template rendering

    context = {
        "sales": sales
    }

    return render(request, "all_sales.html", context)

def search_sales(request):
    
    #searching sales based on query parameters
    product = request.GET.get("product", "").strip()
    category = request.GET.get("category", "").strip()
    salesperson = request.GET.get("salesperson", "").strip()
    region = request.GET.get("region", "").strip()
    date = request.GET.get("date", "").strip()
    
    sales = search_sales_db(
        product=product,
        category=category,
        salesperson=salesperson,
        region=region,
        date=date
    )

    for sale in sales:
        sale['id'] = str(sale['_id'])

    context = {
            "sales": sales,
            "query_params": {
            "product": product,
            "category": category,
            "salesperson": salesperson,
            "region": region,
            "date": date,
        }
    }

    return render(request, "search_sales.html", context)

def delete_sale_view(request, sale_id):
    """
    Shows confirmation on GET, deletes record from MongoDB on POST.
    """
    if request.method == "POST":
        delete_sale_db(sale_id)
        messages.success(request, "Sale record deleted successfully!")
        return redirect("search_sales")

    # Retrieve record details for confirmation page
    sale = sales_collection.find_one({"_id": ObjectId(sale_id)})
    if sale:
        sale["id"] = str(sale["_id"])
    else:
        return redirect("search_sales")

    return render(request, "delete_sale.html", {"sale": sale})


def update_sale_view(request, sale_id):
    """
    Displays the edit form and updates the sale data in MongoDB.
    """
    if request.method == "POST":
       # get the updated data from the form
        new_date = request.POST.get("date")
        new_salesperson = request.POST.get("salesperson")
        new_region = request.POST.get("region")
        new_category = request.POST.get("category")
        new_product = request.POST.get("product")
        new_quantity = int(request.POST.get("quantity", 0))
        new_unit_price = float(request.POST.get("unit_price", 0.0))

       #update the sale in the database
        update_sale_db(
            sale_id,
            new_date,
            new_salesperson,
            new_region,
            new_category,
            new_product,
            new_quantity,
            new_unit_price
        )
        messages.success(request, "Sale record updated successfully!")
        return redirect("search_sales")

   
    sale = sales_collection.find_one({"_id": ObjectId(sale_id)})
    sale["id"] = str(sale["_id"])

    return render(request, "update_sale.html", {"sale": sale})

def add_sale_view(request):
    """
    Renders form on GET and creates a new sale record in MongoDB on POST.
    """
    if request.method == "POST":
        date = request.POST.get("date")
        salesperson = request.POST.get("salesperson")
        region = request.POST.get("region")
        category = request.POST.get("category")
        product = request.POST.get("product")
        quantity = int(request.POST.get("quantity", 1))
        unit_price = float(request.POST.get("unit_price", 0.0))

        # Chama a função add_sale original do seu crud.py
        add_sale_db(
            date=date,
            salesperson=salesperson,
            region=region,
            category=category,
            product=product,
            quantity=quantity,
            unit_price=unit_price
        )

        messages.success(request, "New sale record added successfully!")
        return redirect("search_sales")

    return render(request, "add_sale.html")

def dashboard_view(request):
    """
    Gets data from MongoDB, processes it with Pandas, and renders the Dashboard page.
    """
    records = get_all_sales()
    
    if not records:
        context = {"empty_data": True}
        return render(request, "dashboard.html", context)

    # Convert the list of records to a Pandas DataFrame
    df = pd.DataFrame(records)
    
    # Data cleaning and preparation
    df = df.drop_duplicates()
    df["Date"] = pd.to_datetime(df["Date"])    
    
    if "Sales" not in df.columns:
        df["Sales"] = df["Quantity"] * df["UnitPrice"]

    # --- Summary Metrics ---
    total_sales = float(df["Sales"].sum())
    average_sale = float(df["Sales"].mean())
    highest_sale = float(df["Sales"].max())
    lowest_sale = float(df["Sales"].min())
    total_transactions = len(df)

    # --- Category Analysis ---
    category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
    top_category = category_sales.index[0] if not category_sales.empty else "N/A"
    
    categories_labels = category_sales.index.tolist()
    categories_values = category_sales.values.tolist()

    # --- Monthly Analysis ---
    df["Month_Name"] = df["Date"].dt.month_name()
    df["Month_Num"] = df["Date"].dt.month
    
    # Organizes monthly sales by month number to ensure correct order in the chart
    monthly_sales = df.groupby(["Month_Num", "Month_Name"])["Sales"].sum().reset_index().sort_values("Month_Num")
    
    top_month_row = monthly_sales.loc[monthly_sales["Sales"].idxmax()] if not monthly_sales.empty else None
    top_month = top_month_row["Month_Name"] if top_month_row is not None else "N/A"

    months_labels = monthly_sales["Month_Name"].tolist()
    months_values = monthly_sales["Sales"].tolist()

    context = {
        "total_sales": total_sales,
        "average_sale": average_sale,
        "highest_sale": highest_sale,
        "lowest_sale": lowest_sale,
        "total_transactions": total_transactions,
        "top_category": top_category,
        "top_month": top_month,       
        "cat_labels": categories_labels,
        "cat_data": categories_values,
        "month_labels": months_labels,
        "month_data": months_values,
    }

    return render(request, "dashboard.html", context)