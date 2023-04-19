
import mysql.connector  #helps to connect mysql database using python
#connect mysql server running on the local machine
mydb = mysql.connector.connect(
  host="localhost",
  user="****",
  password="****",
  database="sportsanalyst"
)
#create cursor object it is used to execute sql queries and fetch the data
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE sportsanalyst")
#mycursor.execute("CREATE TABLE CUSTOMER ( NAME VARCHAR(255), ADDRESS VARCHAR(255))")
#mycursor.execute("SHOW TABLES")
#mycursor.execute("ALTER TABLE CUSTOMER ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY")
edata ="INSERT INTO CUSTOMER (NAME, ADDRESS) VALUES (%s,%s)"
evals =("aswin","salem")
mycursor.execute(edata,evals)
mydb.commit() # commit the current changes
