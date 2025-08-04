import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('ecommerce.db')

# Clear existing users to avoid duplicate primary key error
cursor = conn.cursor()
cursor.execute("DELETE FROM users")
conn.commit()

# Load users.csv
users_df = pd.read_csv('users.csv')
users_df.to_sql('users', conn, if_exists='append', index=False)

print("Users data loaded successfully.")

conn.close()
