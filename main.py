import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root",database="miniempp")
print("Enter a Unique Id")
id=int(input())
print("Enter first Name")
firstname=input()
print("Enter last Name")
lastname=input()
print("Enter Regno")
regno=int(input())
mycursor = mydb.cursor()
SQLCommand = ("INSERT INTO emp(id,firstname,lastname,regno) values(%s,%s,%s,%s)")
values=[id,firstname,lastname,regno]
mycursor.execute(SQLCommand,values)
mydb.commit()
print("Data Successfully Inserted")
mydb.close()