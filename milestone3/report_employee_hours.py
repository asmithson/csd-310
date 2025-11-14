import mysql.connector
from decimal import Decimal

# Connecting to Database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TakaisBae25!",
    database="bacchus_winery_v2",
)

cursor = connection.cursor()


def report_employee_hours():
    print("\n---- EMPLOYEE HOURS PER QUARTER ----")

    query = """
    SELECT
        CONCAT(e.First_Name, ' ', e.Last_Name) AS Employee_Name,
        d.Dept_Name,
        eh.Year,
        eh.Quarter,
        SUM(eh.Hours_Worked) AS Total_Hours
    FROM Employee_Hour eh
    JOIN Employee e ON eh.Employee_ID = e.Employee_ID
    JOIN Department d ON e.Dept_ID = d.Dept_ID
    GROUP BY e.Employee_ID, d.Dept_Name, eh.Year, eh.Quarter
    ORDER BY d.Dept_Name, e.Employee_ID, eh.Year, eh.Quarter;
    """

    try:
        cursor.execute(query)
        rows = cursor.fetchall()

        if rows:
            print("Employee_Name | Dept_Name | Year | Quarter | Total_Hours")
            for row in rows:
                clean_row = []
                for value in row:
                    if isinstance(value, Decimal):
                        value = float(value)
                    clean_row.append(value)

                print(tuple(clean_row))
        else:
            print("No employee hour records found.")
        
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")


# Run the report
report_employee_hours()

# Close the connection
cursor.close()
connection.close()

# References (for instructor only):
#
# Liang, Y. D. (2020). Introduction to Java programming and data structures (13th ed.,
# Chapter 2: Elementary Programming). Pearson.
#
# Liang, Y. D. (2020). Introduction to Java programming and data structures (13th ed.,
# Chapter 4: Characters and Strings). Pearson.
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
# W3Schools. (n.d.). Python strings. https://www.w3schools.com/python/python_strings.asp
