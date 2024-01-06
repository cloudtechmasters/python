import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="testdb",
    port=3306
)

print(mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO employee (emp_id,emp_name,emp_sal) VALUES (%s, %s, %s)"
# val = (100, "Tushar",1000)
# mycursor.execute(sql, val)
# To insert multiple records we need to create list of tuples and use executemay
listoftuples = [(101, "hrushi",2000),(200, "vihan",1200),(300, "ramesh",1500)]
mycursor.executemany(sql,listoftuples)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
