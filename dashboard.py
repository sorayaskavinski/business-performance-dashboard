"""
Business Performance Dashboard 

Module: 2 - Cloud Database Integration

Author: Soraya Skavinski

This program loads a sales dataset from a MongoDB database and displays basic information about the data.
"""

import pandas as pd
import matplotlib.pyplot as plt
from database.database import get_sales 

# Terminal formatting
BOLD = "\033[1m"
RESET = "\033[0m"

def load_data_from_mongodb():
    """
    Load sales data from MongoDB into a Pandas DataFrame.
    """
   
    records = get_sales()
   
    df = pd.DataFrame(records)
    
    df["Date"] = pd.to_datetime(df["Date"])
    
    return df


def clean_data(df):
    """
    Check and clean the dataset.
    """

    print("\n===== DATA CLEANING =====")

    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Check for duplicate rows
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicates}")

    # Remove duplicates if any exist
    if duplicates > 0:
        df = df.drop_duplicates()
        print("Duplicate rows removed.")

    print("\nData cleaning completed.")

    return df

def display_dataset_info(df):
    """
    Display basic information about the dataset.

    Args:
        df (DataFrame): The sales dataset.
    """
    print("\n===== FIRST 5 ROWS =====")
    print(df.head())

    print("\n===== DATASET INFORMATION =====")
    df.info()

    
def display_summary(df):
    """
    Display business summary statistics.
    """

    print("\n" + "=" * 50)
    print(f"{BOLD}BUSINESS SUMMARY{RESET}")
    print("=" * 50)

    total_sales = df["Sales"].sum()
    average_sale = df["Sales"].mean()
    highest_sale = df["Sales"].max()
    lowest_sale = df["Sales"].min()
    total_transactions = len(df)

    print(f"Total Sales:           ${total_sales:,.2f}")
    print(f"Average Sale:          ${average_sale:,.2f}")
    print(f"Highest Sale:          ${highest_sale:,.2f}")
    print(f"Lowest Sale:           ${lowest_sale:,.2f}")
    print(f"Transactions:          {total_transactions}")


def sales_by_category(df):
    """
    Determine which product category generated the highest sales and display the results.
    """

    print("\n" + "=" * 50)
    print("QUESTION 1")
    print("=" * 50)

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )
    print("Which product category generated the highest sales?\n")
    top_category = category_sales.idxmax()
    print(f"\nTop Category: {BOLD}{top_category}{RESET}")

def sales_by_month(df):
    """
    Determine which month generated the highest sales.
    """

    print("\n" + "=" * 50)
    print("QUESTION 2")
    print("=" * 50)    

    monthly_sales = (
        df.groupby(df["Date"].dt.month_name())["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print(f"{BOLD}Which month generated the highest sales?\n{RESET}")
    top_month = monthly_sales.idxmax()
    print(f"Top Month: {BOLD}{top_month}{RESET}")

def create_category_chart(df):
    """
    Create a bar chart showing total sales by category.
    """

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8,5))

    category_sales.plot(kind="bar")

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")

    plt.tight_layout()

    plt.savefig("charts/category_sales.png")

    plt.close()

    print("\nCategory chart saved to charts/category_sales.png")

def create_monthly_chart(df):
    """
    Create a line chart showing monthly sales.
    """

    monthly_sales = (
        df.groupby(df["Date"].dt.month)["Sales"]
        .sum()
    )

    plt.figure(figsize=(9,5))

    monthly_sales.plot(kind="line", marker="o")

    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")

    plt.xticks(range(1,13))

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("charts/monthly_sales.png")

    plt.close()

    print("Monthly chart saved to charts/monthly_sales.png")

def run_dashboard():
    """
    Run the Business Performance Dashboard.
    """

    print("=" * 50)
    print("      BUSINESS PERFORMANCE DASHBOARD")
    print("=" * 50)

    sales_df = load_data_from_mongodb()

    sales_df = clean_data(sales_df)

    display_dataset_info(sales_df)

    display_summary(sales_df)

    sales_by_category(sales_df)

    sales_by_month(sales_df)

    create_category_chart(sales_df)

    create_monthly_chart(sales_df)

    print("\nAnalysis completed successfully.")