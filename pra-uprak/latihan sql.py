import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sakola2"
)

if mydb.is_connected():
    print("cihuyy")
    
name = input("Enter name: ")
nis = input("Enter NIS: ")
nisn = input("Enter NISN: ")
        
cursor = mydb.cursor()

sql = "INSERT INTO user (nama, nis, nisn) VALUES (%s, %s, %s)"
data = (name, nis, nisn)

cursor.execute(sql, data)
mydb.commit()
print(f"User {name} created successfully.")