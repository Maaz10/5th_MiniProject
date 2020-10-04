import mysql.connector
from datetime import datetime
from datetime import time
from datetime import timedelta

mydb = mysql.connector.connect(
    host="localhost", user="root", password="12345", database="miniproject")
mycursor = mydb.cursor()

#Get current ime in Y-M-D H:M:S.F format
ytime = datetime.now()
xy = str(ytime)
current_time = ytime.strptime(xy, "%Y-%m-%d  %H:%M:%S.%f")
hor = current_time.hour
mins = current_time.minute
secs = current_time.second

#Changed From Ytime to Ctime as datetime and time delta values structures
ctime = timedelta(hours=hor, minutes=mins, seconds=secs)  # time object
employeeID = 0
cl_time = timedelta(hours=10, minutes=45, seconds=00)


def Buffer():
    for x in range(100):
        print('_', end=' ')
    print("""\n
        Welcome To DSU Attendance System !!!
        """)
    employeeID = int(input("          Enter your employee ID: "))
    my_select_query = "Select * from details where ssn=%s"
    mycursor.execute(my_select_query, (employeeID,))
    records = mycursor.fetchall()
    for x in records:
            Name = x[1]
            print("\n            Good Morning Prof.", Name,'\n')

# Assign the default college timings and converting it into minutes
    default_College_Time = timedelta(hours=8, minutes=45, seconds=00)
    print("            Actual college time is:", default_College_Time)
    default_College_Time_min = default_College_Time.total_seconds()/60


# update function called whenever remanining buffer has to be updated


    def update_buffer():
        updateBufferQuery = "Update details set bufferTime =%s where ssn=%s"
        mycursor.execute(updateBufferQuery, (RemainingBufferTime, employeeID,))
        mydb.commit()
        mycursor.execute(my_select_query, (employeeID,))
        records = mycursor.fetchall()

        for x in records:
            BufferTime = x[3]
            print("             Buffer time remaining is : ", BufferTime)

    for x in records:
        punchInTime = ctime
        print("            punchInTime: ", punchInTime)
        punchInTimeInMinutes = punchInTime.total_seconds()/60
        default_buffer_Time_min = x[3]
        print("            Buffer Time is: ", default_buffer_Time_min)
        # condition to check deduct CL if remaining buffer time is 0.
        if default_buffer_Time_min == 0:
            cl = x[-2]
            # Decrease CL
            if cl > 0:
                cl -= 1
                print("            Cl is deducted")
                sql = ("Update details set NoOfCl =%s where ssn=%s")
                mycursor.execute(sql, (cl, employeeID,))
                print("            remaining CL is :", cl)
                mydb.commit()
                exit()
            else:
                # Deduct Salary after Cl becomes 0 and Refresh Cl
                print("            No cl left in the account\nSalary deducted\n\n")
                sal = x[-1]
                sal -= 1
                sql = ("Update details set salary_decrease =%s where ssn=%s")
                mycursor.execute(sql, (sal, employeeID,))
                sql = ("Update details set Noofcl =%s where ssn=%s")
                mycursor.execute(sql, (cl, employeeID,))
                mydb.commit()
                exit()

    # Calculate the time difference to update the buffer
        TimeDifference = punchInTimeInMinutes-default_College_Time_min
        print("            The time difference in minutes :", TimeDifference)

    # case1 when the employee is on time or before time / TimeDifference <=0
        if (TimeDifference <= 0):
            
            updateBufferQuery = "Update details set bufferTime =%s where ssn=%s"
            mycursor.execute(updateBufferQuery,
                             (default_buffer_Time_min, employeeID,))
            mydb.commit()
            mycursor.execute(my_select_query, (employeeID,))
            records = mycursor.fetchall()

            for x in records:
                BufferTime = x[3]
                print("            Buffer time remaining is : ", BufferTime)
    # case2 when the employee is little late or before time / TimeDifference <= 120
        elif (TimeDifference <= default_buffer_Time_min):
            RemainingBufferTime = default_buffer_Time_min - TimeDifference
            update_buffer()

    # case3 when the employee has arrived after 120 minutes of buffer  / TimeDifference > 120
        elif (TimeDifference >= default_buffer_Time_min):
            RemainingBufferTime = 0
    print("\n          Thank you !! Have a nice day !!!")
    sql = ("Update details set punchIn =%s where ssn=%s")
    mycursor.execute(sql, (ctime, employeeID,))
    mydb.commit()
