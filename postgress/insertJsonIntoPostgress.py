import psycopg2
import json


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


sql = "INSERT INTO employee (emp_id,emp_name,emp_sal) VALUES (%s, %s, %s)"

listOfTuples=[]
with open('employee.json','r') as json_file:
    data=json.load(json_file)
    print(data)
    for row in data:
        print(row)
        listOfTuples.append(tuple(row.values()))
    print(listOfTuples)

    cur.executemany(sql, listOfTuples)
    # Commit the changes
    conn.commit()

    print(cur.rowcount, "record inserted.")

    # Close the cursor and connection
    cur.close()
    conn.close()