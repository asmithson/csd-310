import mysql.connector

# Connecting to Database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TakaisBae25!",
    database="bacchus_winery"
)

cursor = connection.cursor()

def report_supplier_delivery():
    print("\n---- SUPPLIER DELIVERY PERFORMANCE ----")
    
    query = """
    SELECT
        s. Supplier_Name,
        sh.Shipment_ID,
        sh.Expected_Delivery,
        sh.Actual_Delivery,
        sh.Delivery_Status,
        DATEDIFF(sh.Actual_Delivery, sh.Expected_Delivery) AS Days_Late,
        DATE_FORMAT(sh.Expected_Delivery, '%Y-%m') AS Delivery_Month
    FROM Shipment sh
    JOIN Supplier s ON sh.Supplier_ID = s.Supplier_ID
    ORDER BY sh.Expected_Delivery;
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    if rows:
        for row in rows:
            print(row)
    else:
        print("No delivery records found.")

# Function to run the report
report_supplier_delivery()

# Closing the connection
cursor.close()
connection.close()