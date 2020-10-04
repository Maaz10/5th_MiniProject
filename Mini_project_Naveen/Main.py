"""
-------------------------------Pre-Requisits ---------------------------
Pre Processing.py File must be run Before running this file to Initialize a Test Case
Run the Below Comands:
->create database miniproject
->create table details (ssn int primary key, name varchar(20) , punchIn varchar(30) , bufferTime int , NoOfCl int);
Install mysql library pip install mysql-connector-python
"""

#import Mysql library
import mysql.connector

#Connection with database
mydb = mysql.connector.connect(host="localhost", user="root", password="Shreeki123*",database="miniproject")
mycursor = mydb.cursor()

if __name__ == "__main__":
    for i in mycursor:
        print(i)
    testValue = 1

    #while loop for unlimited re-attempts
    while testValue == 1:
        print("""\n
        Welcome To DSU Attendance System !!!
        """)
        employeeID = int(input("\n        Please Enter your employee ID: "))
        sql = "Select * from details where ssn=%s"
        mycursor.execute(sql, (employeeID,))

        for x in mycursor:
            cl = x[-2]
            if cl > 0 :

                #Decrease CL
                cl-=1
                print("           Cl is deducted")
                sql = ("Update details set Noofcl =%s where ssn=%s")
                mycursor.execute(sql, (cl, employeeID,))
                print("           remaining CL is :",cl)
            
            else:

                #Deduct Salary after Cl becomes 0 and Refresh Cl
                print("           No cl left in the account\n           Salary deducted\n\n")
                sal = x[-1]
                sal-=1
                sql = ("Update details set salary_decrease =%s where ssn=%s")
                mycursor.execute(sql, (sal, employeeID,))
                cl=15
                sql = ("Update details set Noofcl =%s where ssn=%s")
                mycursor.execute(sql, (cl, employeeID,))
        for i in mycursor:
            print(i)
        mydb.commit()
    mydb.close()
