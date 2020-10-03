"""
-------------------------------Pre-Requisits ---------------------------
Pre Processing.py File must be run Before running this file to Initialize a Test Case
Run the Below Comands:
->create database miniproject
->create table details (ssn int primary key, name varchar(20) , punchIn varchar(30) , bufferTime int , NoOfCl int);
Install mysql library pip install mysql-connector-python
"""

#Import sql library
import mysql.connector

#Table Prarameters (ssn int primary key, name varchar(20) , punchIn varchar(30) , bufferTime int , NoOfCl int)

#Connection with database
mydb = mysql.connector.connect(host="localhost", user="root", password="12345",database="miniproject")

#Take Inputs
print("Enter a SSN")
ssn=int(input())
print("Enter Name")
name=input()
bufferTime=120
punchIn='08:45'
NoOfCl=15

#Run Command To Insert
mycursor = mydb.cursor()
SQLCommand = ("INSERT INTO details values(%s,%s,%s,%s,%s)")
values=[ssn,name,punchIn,bufferTime,NoOfCl]
mycursor.execute(SQLCommand,values)
mydb.commit()
print("Data Successfully Inserted")
mydb.close()