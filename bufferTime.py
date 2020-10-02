import mysql.connector
from datetime import timedelta
#Connecting to mySQL server.
mydb = mysql.connector.connect(host="localhost",  user="root", passwd="********", database="Faculty")
mycursor = mydb.cursor(buffered=True)

#Getting the Punch in time from entered employee ID.
empID = int(input("Enter your employee ID: "))
my_select_query = "Select * from employeeDetails where empID=%s"
mycursor.execute(my_select_query, (empID,))
records = mycursor.fetchall()

for x in records:
    punchInTime = x[2]
    print("punchInTime: ", punchInTime)

punchInTimeInMinutes = punchInTime.total_seconds()/60
print("Punch in time in minutes: ", punchInTimeInMinutes)

#Assign the default college timings and converting it into minutes

default_College_Time = timedelta(hours = 8, minutes = 45, seconds = 00)
print("Actual college time is:", default_College_Time)
default_College_Time_min = default_College_Time.total_seconds()/60
print("College time in minutes:", default_College_Time_min)

#Assign the default buffer timings and converting it into minutes

default_buffer_Time = timedelta(hours = 2, minutes = 00, seconds = 00)
print("Provided buffer time is:", default_buffer_Time)
default_buffer_Time_min = default_buffer_Time.total_seconds()/60
print("Buffer time in minutes: ", default_buffer_Time_min)

#Calculate the time difference to update the buffer

TimeDifference = punchInTimeInMinutes-default_College_Time_min
print("The time difference in minutes :", TimeDifference)

#update function called whenever remanining buffer has to be updated

def update_buffer():
    updateBufferQuery = "Update employeeDetails set BufferTime =%s where empID=%s"
    mycursor.execute(updateBufferQuery, (RemainingBufferTime, empID,))
    mydb.commit()
    mycursor.execute(my_select_query, (empID,))
    records = mycursor.fetchall()

    for x in records:
        BufferTime = x[3]
        print("Buffer time remaining is : ", BufferTime)


#case1 when the employee is on time or before time / TimeDifference <=0

if(TimeDifference <= 0):
    print("Thank you !! Have a nice day.")
    updateBufferQuery="Update employeeDetails set BufferTime =%s where empID=%s"
    mycursor.execute(updateBufferQuery, (default_buffer_Time_min , empID ,))
    mydb.commit()
    mycursor.execute(my_select_query, (empID,))
    records = mycursor.fetchall()

    for x in records:
        BufferTime = x[3]
        print("Buffer time remaining is : ", BufferTime)
#case2 when the employee is little late or before time / TimeDifference <= 120

elif(TimeDifference <= default_buffer_Time_min):
    RemainingBufferTime = default_buffer_Time_min - TimeDifference
    update_buffer()

#case3 when the employee has arrived after 120 minutes of buffer  / TimeDifference > 120

elif(TimeDifference >= default_buffer_Time_min):
    RemainingBufferTime = 0
    update_buffer()


