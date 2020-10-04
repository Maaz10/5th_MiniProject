import mysql.connector
from datetime import datetime
from datetime import time
from datetime import timedelta
from Buffer import Buffer

#Connection To Database Server
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
ctime = default_College_Time = timedelta(
    hours=hor, minutes=mins, seconds=secs)  # time object

cl_time = timedelta(hours=10, minutes=45, seconds=00)



# while loop for unlimited re-attempts
testValue = 1
while testValue == 1:
    Buffer()
