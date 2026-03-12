# Write a Python program to subtract five days from current date.
import datetime
x = datetime.datetime.now()

a = x - datetime.timedelta(days=5)  #day-5

print(a)

# Write a Python program to print yesterday, today, tomorrow.
import datetime
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)

# Write a Python program to drop microseconds from datetime.
import datetime
x = datetime.datetime.now()
m = x.replace(microsecond=0)
print(m)

# Write a Python program to calculate two date difference in seconds.
from datetime import *
current = datetime(2022, 12, 11, 13, 24, 15)
second = datetime(2021, 10, 24, 13, 15, 21)
difference = current - second
total = difference.total_seconds()
print(total)

