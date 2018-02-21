import csv
import MySQLdb
import sys

input_file = sys.argv[1]

con = MySQLdb.connect(host = 'localhost', port = 3306, db = 'my_suppliers', user = 'root', passwd = '1234')
c = con.cursor()

file_reader = csv.reader(open(input_file, 'r', newline=''), delimiter = ',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)
    c.execute("""DELETE FROM Suppliers WHERE Supplier_Name='Supplier X'""")
con.commit()

c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)