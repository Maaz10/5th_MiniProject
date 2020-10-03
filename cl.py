import mysql.connector

def timetoInt(t):
    result = (t[0]+t[1])* 60 +t[2]
    return result

if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tejashjl"
    )
    mycursor = mydb.cursor()

    mycursor.execute("drop database employee")
    mycursor.execute("CREATE DATABASE employee")



    mycursor.execute("USE employee")

    mycursor.execute("create table details (ssn int primary key, name varchar(200) , punchIn varchar(300) , bufferTime int , NoOfCl int) ")
    sql = "INSERT INTO details (ssn,name,punchIn,bufferTime,NoOfCl) VALUES (%s, %s,%s,%s,%s)"
    val = ('1','Hermoine','08:45','120','15')
    mycursor.execute(sql, val)
    val = ('2', 'Harry', '09:45', '120','10')
    mycursor.execute(sql, val)
    val = ('3', 'Ron', '10:45', '120','1')
    mycursor.execute(sql, val)
    val = ('4', 'Snape+++', '11:45', '120','0')
    mycursor.execute(sql, val)
    mycursor.execute("select * from details")
    for i in mycursor:
        print(i)
    testValue = 1
    while testValue == 1:
        employeeID = int(input("\nEnter your employee ID: "))
        sql = "Select * from details where ssn=%s"
        mycursor.execute(sql, (employeeID,))

        for x in mycursor:
            cl = x[-1]
            print("\nNumber of CL currently available:",cl)
            if cl > 0 :
                cl-=1
                print("\nCl is deducted")
                sql = "Update details set Noofcl =%s where ssn=%s"
                mycursor.execute(sql, (cl, employeeID,))
                print("\n\nremaining CL is :",cl)
            else:
                print("No cl left in the account\n\nSalary deducted\n\n")

        mycursor.execute("select * from details")
        for i in mycursor:
            print(i)
        testValue = int(input("Enter 1 to continue"))