import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('ecommerce.db')

# --- Check number of records in users ---
users_count = pd.read_sql_query("SELECT COUNT(*) as total_users FROM users", conn)
print("Total users:", users_count['total_users'][0])

# --- Preview first 5 users ---
print("\nSample users data:")
print(pd.read_sql_query("SELECT * FROM users LIMIT 5", conn))

# --- Check number of records in orders ---
orders_count = pd.read_sql_query("SELECT COUNT(*) as total_orders FROM orders", conn)
print("\nTotal orders:", orders_count['total_orders'][0])

# --- Preview first 5 orders ---
print("\nSample orders data:")
print(pd.read_sql_query("SELECT * FROM orders LIMIT 5", conn))

# Close connection
conn.close()
