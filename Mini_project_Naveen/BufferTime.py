import mysql.connector
from datetime import timedelta
#Connecting to mySQL server.
mydb = mysql.connector.connect(host="localhost",  user="root", passwd="Shreeki123*", database="miniproject")
mycursor = mydb.cursor(buffered=True)

#Getting the Punch in time from entered employee ID.
empID = int(input("Enter your employee ID: "))
my_select_query = "Select * from details where ssn=%s"
mycursor.execute(my_select_query, (empID,))
records = mycursor.fetchall()

#Assign the default college timings and converting it into minutes
default_College_Time = timedelta(hours = 8, minutes = 45, seconds = 00)
print("Actual college time is:", default_College_Time)
default_College_Time_min = default_College_Time.total_seconds()/60


#update function called whenever remanining buffer has to be updated
def update_buffer():
    updateBufferQuery = "Update details set bufferTime =%s where ssn=%s"
    mycursor.execute(updateBufferQuery, (RemainingBufferTime, empID,))
    mydb.commit()
    mycursor.execute(my_select_query, (empID,))
    records = mycursor.fetchall()

    for x in records:
        BufferTime = x[3]
        print("Buffer time remaining is : ", BufferTime)


for x in records:
    punchInTime = x[2]
    print("punchInTime: ", punchInTime)
    punchInTimeInMinutes = punchInTime.total_seconds()/60
    default_buffer_Time_min = x[3]
    print("Buffer Time is: ", default_buffer_Time_min)
    #condition to check deduct CL if remaining buffer time is 0.
    if default_buffer_Time_min == 0:
        cl = x[-2]
        #Decrease CL
        if cl > 0:
            cl -= 1
            print("Cl is deducted")
            sql = ("Update details set NoOfCl =%s where ssn=%s")
            mycursor.execute(sql, (cl, empID,))
            print("remaining CL is :", cl)
            mydb.commit()
            exit()
        else:
            # Deduct Salary after Cl becomes 0 and Refresh Cl
                print("No cl left in the account\nSalary deducted\n\n")
                sal = x[-1]
                sal-=1
                sql = ("Update details set salary_decrease =%s where ssn=%s")
                mycursor.execute(sql, (sal, empID,))
                cl=15
                sql = ("Update details set Noofcl =%s where ssn=%s")
                mycursor.execute(sql, (cl, empID,))
                mydb.commit()
                exit()

    #Calculate the time difference to update the buffer
    TimeDifference = punchInTimeInMinutes-default_College_Time_min
    print("The time difference in minutes :", TimeDifference)

    # case1 when the employee is on time or before time / TimeDifference <=0
    if (TimeDifference <= 0):
        print("Thank you !! Have a nice day.")
        updateBufferQuery = "Update details set bufferTime =%s where ssn=%s"
        mycursor.execute(updateBufferQuery, (default_buffer_Time_min, empID,))
        mydb.commit()
        mycursor.execute(my_select_query, (empID,))
        records = mycursor.fetchall()

        for x in records:
            BufferTime = x[3]
            print("Buffer time remaining is : ", BufferTime)
    # case2 when the employee is little late or before time / TimeDifference <= 120
    elif (TimeDifference <= default_buffer_Time_min):
        RemainingBufferTime = default_buffer_Time_min - TimeDifference
        update_buffer()

    # case3 when the employee has arrived after 120 minutes of buffer  / TimeDifference > 120
    elif (TimeDifference >= default_buffer_Time_min):
        RemainingBufferTime = 0












