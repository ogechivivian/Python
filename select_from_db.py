import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ISW-ENGR-OV1\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM TestDB.dbo.Users')

for row in cursor:
    print(row)


