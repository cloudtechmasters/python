import psycopg2
import csv

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="vPjHG2maFp",
    host="127.0.0.1",
    port="5432"
)

# Create a cursor
cur = conn.cursor()

# Define the path to your CSV file
csv_file_path = "employees.csv"

sql = "INSERT INTO employee (emp_id,emp_name,emp_sal) VALUES (%s, %s, %s)"

listOfTuples = []
# Read data from CSV and insert into PostgreSQL
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    print(csv_reader)
    headers = next(csv_reader)
    for row in csv_reader:
        print(row)
        listOfTuples.append(tuple(row))

    print(listOfTuples)

cur.executemany(sql,listOfTuples)
# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
