import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('ecommerce.db')

# Clear existing data to avoid duplicate primary key error
cursor = conn.cursor()
cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM orders")
conn.commit()

# Load users.csv
users_df = pd.read_csv('users.csv')
users_df.to_sql('users', conn, if_exists='append', index=False)
print("Users data loaded successfully.")

# Load orders.csv
orders_df = pd.read_csv('orders.csv')
orders_df.to_sql('orders', conn, if_exists='append', index=False)
print("Orders data loaded successfully.")

conn.close()
