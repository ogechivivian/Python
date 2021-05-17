import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ISW-ENGR-OV1\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM TestDB.dbo.Users')

cursor.execute('''
                INSERT INTO TestDB.dbo.Users (FirstName, Age, City)
                VALUES
                ('Bob',55,'Montreal'),
                ('Jenny',66,'Boston')
                ''')
conn.commit()