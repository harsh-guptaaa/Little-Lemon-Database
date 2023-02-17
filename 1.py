import mysql.connector as connector
connection = connector.connect(user='root', 
                               database='LittleLemonDB', 
                               password='jiayou77.', 
                               auth_plugin='mysql_native_password')
# create a cursor object
cursor = connection.cursor()

# create a variable to hold the query
show_tables_query = """SHOW TABLES"""

# execute the query
cursor.execute(show_tables_query)

# print out the results
results = cursor.fetchall()

print(results)

select_statement = """
SELECT 
    CONCAT(c.FirstName, c.LastName) AS FullName,
    c.Email,
    c.ContactNumber
FROM Customers AS c
INNER JOIN Orders AS o USING(CustomerID)
WHERE o.BillAmount > 60;
"""

cursor.execute(select_statement)

results = cursor.fetchall()
print(cursor.column_names)
for result in results:
    print(result)
