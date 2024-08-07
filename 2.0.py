import numpy as np


def print_array(array, message=''):
    if message:
        print(message)
    print(array)
    print('\n')


# 1. Array Creation:
# Generate a multi-dimensional NumPy array with predefined values to simulate e-commerce transactions.
# The array should include transaction_id, user_id, product_id, quantity, price, and timestamp.

data = np.array([
    [1, 101, 501, 2, 20.5, '2024-08-01'],
    [2, 102, 502, 1, 15.0, '2024-08-01'],
    [3, 103, 503, 3, 22.0, '2024-08-02'],
    [4, 104, 501, 0, 20.5, '2024-08-02'],
    [5, 101, 504, 1, 30.0, '2024-08-03'],
    [6, 102, 502, 4, 15.0, '2024-08-03']
], dtype=object)


# 2. Data Analysis Functions:
def total_revenue(data):
    revenue = np.sum(data[:, 3].astype(float) * data[:, 4].astype(float))
    return revenue


def unique_users(data):
    users = np.unique(data[:, 1])
    return len(users)


def most_purchased_product(data):
    product_ids, quantities = np.unique(data[:, 2], return_counts=True)
    most_purchased = product_ids[np.argmax(quantities)]
    return most_purchased


def convert_price_to_int(data):
    data[:, 4] = data[:, 4].astype(int)
    return data


def check_data_types(data):
    types = [data[:, i].dtype for i in range(data.shape[1])]
    return types


# 3. Array Manipulation Functions:
def product_quantity_array(data):
    return data[:, [2, 3]]


def user_transaction_count(data):
    unique, counts = np.unique(data[:, 1], return_counts=True)
    return np.array([unique, counts]).T


def masked_array(data):
    mask = data[:, 3].astype(int) > 0
    return data[mask]


# 4. Arithmetic and Comparison Functions:
def price_increase(data, percentage):
    data[:, 4] = data[:, 4].astype(float) * (1 + percentage / 100)
    return data


def filter_transactions(data):
    return data[data[:, 3].astype(int) > 1]


def revenue_comparison(data, start_date1, end_date1, start_date2, end_date2):
    period1 = data[(data[:, 5] >= start_date1) & (data[:, 5] <= end_date1)]
    period2 = data[(data[:, 5] >= start_date2) & (data[:, 5] <= end_date2)]
    revenue1 = total_revenue(period1)
    revenue2 = total_revenue(period2)
    return revenue1, revenue2


# 5. Indexing and Slicing Functions:
def user_transactions(data, user_id):
    return data[data[:, 1] == user_id]


def date_range_slicing(data, start_date, end_date):
    return data[(data[:, 5] >= start_date) & (data[:, 5] <= end_date)]


def top_products(data, top_n=5):
    products, revenue = np.unique(data[:, 2], return_counts=True)
    top_indices = np.argsort(revenue)[-top_n:]
    top_products = products[top_indices]
    return data[np.isin(data[:, 2], top_products)]


# 6. Output Function:
# Already implemented as print_array function above.

# 7. Manipulation Workflow:
def main():
    print_array(data, "Initial e-commerce transactions array:")

    revenue = total_revenue(data)
    print(f"Total Revenue: {revenue}")

    unique_users_count = unique_users(data)
    print(f"Unique Users: {unique_users_count}")

    most_purchased = most_purchased_product(data)
    print(f"Most Purchased Product: {most_purchased}")

    data_int_price = convert_price_to_int(data.copy())
    print_array(data_int_price, "Array with price converted to integer:")

    data_types = check_data_types(data)
    print(f"Data Types of Each Column: {data_types}")

    prod_quantity_array = product_quantity_array(data)
    print_array(prod_quantity_array, "Array with only product_id and quantity columns:")

    user_txn_count = user_transaction_count(data)
    print_array(user_txn_count, "Transaction counts per user:")

    masked_data = masked_array(data)
    print_array(masked_data, "Masked array with non-zero quantity transactions:")

    increased_price_data = price_increase(data.copy(), 5)
    print_array(increased_price_data, "Array with prices increased by 5%:")

    filtered_transactions = filter_transactions(data)
    print_array(filtered_transactions, "Filtered transactions with quantity greater than 1:")

    revenue1, revenue2 = revenue_comparison(data, '2024-08-01', '2024-08-02', '2024-08-02', '2024-08-03')
    print(f"Revenue Comparison:\nPeriod 1: {revenue1}\nPeriod 2: {revenue2}")

    user_transactions_data = user_transactions(data, 101)
    print_array(user_transactions_data, "Transactions for user with ID 101:")

    date_sliced_data = date_range_slicing(data, '2024-08-01', '2024-08-02')
    print_array(date_sliced_data, "Transactions within date range 2024-08-01 to 2024-08-02:")

    top_products_data = top_products(data, top_n=5)
    print_array(top_products_data, "Top 5 products by revenue:")


if __name__ == "__main__":
    main()
