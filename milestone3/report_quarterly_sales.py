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

def report_quarterly_sales():
    print("\n---- QUARTERLY SALES REPORT ----")
    
    query = """
    SELECT
        QUARTER(s.Shipment_Date) AS Quarter,
        SUM(sd.Quantity) AS Total_Units_Sold,
        SUM(sd.Quantity * sd.Unit_Price) AS Total_Revenue
    FROM Shipment s
    JOIN Shipment_Detail sd ON s.Shipment_ID = sd.Shipment_ID
    GROUP BY Quarter
    ORDER BY Quarter;
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    if rows:
        print("Quarter | Total_Units_Sold | Total_Revenue")
        for row in rows:
            clean_row = []
            for value in row:
                if isinstance(value, Decimal):
                    # If the Decimal is a whole number (no decimals)
                    if value == value.to_integral_value():
                        value = int(value)
                    else:                    
                        value = float(value)
                clean_row.append(value)
            
            print(tuple(clean_row))
    else:
        print("No quarterly sales records found.")
        
# Run the report
report_quarterly_sales()

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
#
# W3Schools. (n.d.). Python lists. https://www.w3schools.com/python/python_lists.asp