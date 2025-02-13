import sqlite3
import random
from datetime import datetime, timedelta


# Connect to SQLite
print('Setting up the database....')

conn = sqlite3.connect("mock_database.db")
cursor = conn.cursor()

# Create Departments Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments (
    department_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
""")

# Create Products Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL
);
""")

# Create Customers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    region TEXT NOT NULL
);
""")

# Create Sales Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Sales (
    order_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    price REAL,
    date TEXT,
    department_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES Products (product_id),
    FOREIGN KEY (department_id) REFERENCES Departments (department_id)
);
""")

# Commit and close
conn.commit()
conn.close()


print('Inserting mock data....')

conn = sqlite3.connect("mock_database.db")
cursor = conn.cursor()

# Insert mock data into Departments
departments = [(1, "Electronics"), (2, "Clothing"), (3, "Home & Kitchen")]
cursor.executemany("INSERT INTO Departments VALUES (?, ?)", departments)

# Insert mock data into Products
products = [
    (1, "Laptop", "Electronics"),
    (2, "Smartphone", "Electronics"),
    (3, "T-shirt", "Clothing"),
    (4, "Microwave", "Home & Kitchen")
]
cursor.executemany("INSERT INTO Products VALUES (?, ?, ?)", products)

# Insert mock data into Customers
customers = [(i, f"Customer {i}", random.randint(18, 65), random.choice(["North", "South", "East", "West"])) for i in range(1, 11)]
cursor.executemany("INSERT INTO Customers VALUES (?, ?, ?, ?)", customers)

# Insert mock data into Sales
start_date = datetime(2023, 1, 1)
sales = []
for i in range(1, 21):
    product_id = random.randint(1, 4)
    sales.append((
        i, product_id, random.randint(1, 5), round(random.uniform(20, 500), 2),
        (start_date + timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        random.randint(1, 3)
    ))

cursor.executemany("INSERT INTO Sales VALUES (?, ?, ?, ?, ?, ?)", sales)

conn.commit()
conn.close()
