import csv
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb",
    port=3306
)

print(mydb)

listOfTuples = []
with open('employees.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    print(csv_reader)
    headers = next(csv_reader)
    for row in csv_reader:
        print(row)
        listOfTuples.append(tuple(row))

print(listOfTuples)

myCursor = mydb.cursor()

sql = "INSERT INTO employee (emp_id,emp_name,emp_sal) VALUES (%s, %s, %s)"
myCursor.executemany(sql, listOfTuples)
mydb.commit()

print(myCursor.rowcount, "record inserted.")
