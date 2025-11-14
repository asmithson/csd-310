import mysql.connector
from decimal import Decimal

# Connecting to Database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TakaisBae25!",
    database="bacchus_winery_v2"
)

cursor = connection.cursor()

def report_wine_distribution():
    print("\n---- WINE DISTRIBUTION & SALES ----")
    
    query = """
    SELECT
        p.Wine_Type,
        d.Distributor_Name,
        SUM(sd.Quantity) AS Quantity_Sold,
        SUM(sd.Quantity * sd.Unit_Price) AS Revenue,
        QUARTER(s.Shipment_Date) AS Quarter
    FROM Shipment s
    JOIN Shipment_Detail sd ON s.Shipment_ID = sd.Shipment_ID
    JOIN Product p ON sd.Product_ID = p.Product_ID
    JOIN Distributor d ON s.Distributor_ID = d.Distributor_ID
    GROUP BY p.Wine_Type, d.Distributor_Name, Quarter
    ORDER BY p.Wine_Type, Revenue DESC;
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    if rows:
        print("Wine_Type | Distributor_Name | Quantity_Sold | Revenue | Quarter")
        for row in rows:
            clean_row = []
            for value in row:
                if isinstance(value, Decimal):
                    value = float(value)
                clean_row.append(value)
            
            print(tuple(clean_row))
    else:
        print("No distribution records found.")
        
# Run the report
report_wine_distribution()

# Close the connection
cursor.close()
connection.close()

# References (for instructor only):
#
# Liang, Y. D. (2020). Introduction to Java programming and data structures (13th ed.,
# Chapter 2: Elementary Programming). Pearson.
#
# Liang, Y. D. (2020). Introduction to Java programming and data structures (13th ed.,
# Chapter 5: Loops). Pearson.
#
# W3Schools. (n.d.). Python casting. https://www.w3schools.com/python/python_casting.asp
# 
# W3Schools. (n.d.). Python for loops. https://www.w3schools.com/python/python_for_loops.asp
#
# W3Schools. (n.d.). Python isinstance(). https://www.w3schools.com/python/ref_func_isinstance.asp