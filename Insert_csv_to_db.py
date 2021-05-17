import csv
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ISW-ENGR-OV1\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')
cur = conn.cursor()
with open('demo1.csv', 'r') as f:
    reader = csv.reader(f)
    print(reader)
    # Skip the header row.
    next(reader)
    for row in reader:
        cur.execute(
            "INSERT INTO Users1 VALUES (?, ?, ?, ?)",
            row
        )

conn.commit()

conn.close()
