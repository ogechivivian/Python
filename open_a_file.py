import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ISW-ENGR-OV1\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')

f = open("john.txt", "r")
content = f.read()
print(content)
f.close()
