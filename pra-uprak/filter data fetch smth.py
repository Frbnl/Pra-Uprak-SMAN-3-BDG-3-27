import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sakola"
)

cursor = mydb.cursor()
        
sql = "SELECT * FROM users"
cursor.execute(sql)

results = cursor.fetchmany(1)

print("\n===Users List===")
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    print("--------------------")
    
cursor.fetchall()


cursor = mydb.cursor()
print("specific select")
usid = input("Input ID: ")
sql = "SELECT * FROM users where id=%s"
data = (usid,)

cursor.execute(sql, data)
results = cursor.fetchall()

print("\n===Specific User===")
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    print("--------------------")
