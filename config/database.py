import pyodbc

try:
    connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=zrestaurant.mssql.somee.com;DATABASE=zrestaurant;UID=ssebs_SQLLogin_2;PWD=dzxwtzp6re;Encrypt=no')
    print("Conexión exitosa.")
    cursor = connection.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    print("Versión del servidor de SQL Server: {}".format(row))
    cursor.execute("SELECT 1+2")
    rows = cursor.fetchall()
    print(rows)
    
except Exception as ex:
    print("Error durante la conexión: {}".format(ex))



