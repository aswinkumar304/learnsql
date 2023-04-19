import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="****",
  password="****",
  database="sportsanalyst"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE sportsanalyst")
#mycursor.execute("CREATE TABLE CUSTOMER ( NAME VARCHAR(255), ADDRESS VARCHAR(255))")
#mycursor.execute("SHOW TABLES")
#mycursor.execute("ALTER TABLE CUSTOMER ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY")
sql ="INSERT INTO CUSTOMER (NAME, ADDRESS) VALUES (%s,%s)"
val =("aswin","salem")
mycursor.execute(sql,val)
mydb.commit()
