import mysql.connector

# Connecting to Database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TakaisBae25!",
    database="bacchus_winery"
)

cursor = connection.cursor()

# Function to display any/all tables in the DB
def show_table(table_name):
    print(f"\n---- {table_name.upper()} ----")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    if rows:
        for row in rows:
            print(row)
            
    else:
        print("No records found.")
        
# Displaying all tables in Bacchus Winery DB one at a time
tables = [
    "Department", 
    "Employee", 
    "Employee_Hour", 
    "Supplier", 
    "Distributor", 
    "Product", 
    "Shipment",
    "Shipment_Detail", 
    "Inventory"
]

for t in tables:
    show_table(t)
    
# Closing the connection
cursor.close()
connection.close()
