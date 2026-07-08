"""
Business Performance Dashboard
Module 1 - Data Analysis

Author: Soraya Skavinski

This program loads a sales dataset from a CSV file
and displays basic information about the data.
"""

import pandas as pd


def load_data(file_path):
    """
    Load the CSV file into a Pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        DataFrame: The loaded dataset.
    """
    return pd.read_csv(file_path)


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

    print("\n===== SUMMARY STATISTICS =====")
    print(df.describe())

def sales_by_category(df):
    """
    Display total sales by product category.
    """

    print("\n===== SALES BY CATEGORY =====")

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print(category_sales)

def sales_by_month(df):
    """
    Display total sales by month.
    """

    print("\n===== SALES BY MONTH =====")

    df["Date"] = pd.to_datetime(df["Date"])

    df["Month"] = df["Date"].dt.month_name()

    monthly_sales = (
        df.groupby("Month")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print(monthly_sales)

def main():
    """
    Main function of the program.
    """
    print("=" * 50)
    print("      BUSINESS PERFORMANCE DASHBOARD")
    print("=" * 50)

    data = load_data("data/sales_data.csv")
    display_dataset_info(data)
    sales_by_category(data)
    sales_by_month(data)


if __name__ == "__main__":
    main()