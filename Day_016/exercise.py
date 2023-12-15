from datetime import datetime
from datetime import date

now = datetime.now()
curr_day = now.day
curr_month = now.month
curr_year = now.year
curr_hour = now.hour
curr_min = now.minute
curr_tstamp = now.timestamp()
print(curr_day, curr_hour, curr_min, curr_month, curr_tstamp, curr_year)

t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)

date_str = "5 December, 2019"
date_obj = datetime.strptime(date_str, "%d %B, %Y")
print(date_obj)

new_year = date(year = 2022, month = 1, day = 1)
today = date(year = 2021, month = 9, day = 20)
jan_1970 = date(year = 1970, month = 1, day = 1)
diff = new_year - today
diff2 =-(today - jan_1970) 
print(diff)
print(diff2)