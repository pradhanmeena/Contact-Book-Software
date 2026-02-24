import mysql.connector
from database_details import DatabaseDetails
db=DatabaseDetails()
mydb=mysql.connector.connect(host=db.host,user=db.user,password=db.password,database=db.database)

cur=mydb.cursor()
s="CREATE TABLE phonebook(ref integer(4) primary key ,name varchar(30),gender varchar(10),email varchar(30),mobile varchar(12))"
cur.execute(s)
