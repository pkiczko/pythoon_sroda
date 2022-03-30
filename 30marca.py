#Bibliotek datetime
#materiały z  https://github.com/Asabeneh/30-Days-Of-Python/blob/master/16_Day_Python_date_time/16_python_datetime.md

from datetime import datetime #importowanie modułu datetime

now = datetime.now()
print('Czas teraz: ', now)      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

print('Sekund w roku: ', 60*60*24*365)

#now = datetime.now()
t = now.strftime("%H:%M:%S")

print("t = ", t)
print(now.hour, ':', now.minute, ':', now.second)

from datetime import date
import time

today = date(year=2000, month=2, day=28)
tomorrow = date(year=2000, month=3, day=1)
roznica_czasu = tomorrow - today
# Time left for new year:  27 days, 0:00:00
print('Różnica czasu: ', roznica_czasu)

t1 = datetime(year = now.year, month = now.month, day = now.day, hour = 14, minute = 59, second = 5)
t2 = datetime(year = now.year, month = now.month, day = now.day, hour = 17, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
while(True):
    now=datetime.now()
    print(now.strftime('%H:%M:%S'))
    time.sleep(1)
# wrzucenie czasu do frontend (przy użyciu skryptu JavaScript)
# https://stackoverflow.com/questions/53111362/fun-clock-streaming-text-with-python-and-flask 

#Zadanie - policz czas między teraz a nowym rokiem
