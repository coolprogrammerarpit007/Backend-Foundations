# # Working with dates in Python

# import datetime

# # Working with date -> day,month,year
# # to create a date
# d = datetime.date(2025,10,25)
# # print(d)

# today = datetime.date.today()
# # print(today)

# # print(today.day)
# # print(today.year)
# # print(today.weekday())
# # print(today.isoweekday())


# # Time-deltas -> Time deltas are difference b/w two dates or  times
# t_delta = datetime.timedelta(days=7)
# # print(t_delta)

# future_date = today + t_delta
# # print(future_date)
# time_delta = future_date-today
# # print(time_delta)

# birth_day = datetime.date(2026,5,20)
# # print(birth_day)

# # to get days remaining from today to my birthday
# days_remaining = birth_day - today
# # print(days_remaining)
# # print(days_remaining.days)
# # print(days_remaining.total_seconds())

# # Working with Time

# # creating time
# t1 = datetime.time(9,12,25,4500)
# # print(t1)
# # print(t1.hour)
# # print(t1.minutes)
# # print(t1.seconds)


# # working with date and times together
# # datetime.datetime
# dt = datetime.datetime(2025,11,11,19,30,52,4500)
# # print(dt)
# # print(dt.date())
# # print(dt.time())

# t_delta2 = datetime.timedelta(days=30)
# # print(dt+t_delta2)


# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_ut = datetime.datetime.utcnow()

# # print(dt_today)
# # print(dt_now)
# # print(dt_ut)

# # difference b/w datetime.datetime.today and datetime.datetime.now is that in today() not takes any timezone and get local date-time whereas now can take timezone and get date-time



# Working with the different time-zones

from datetime import datetime
import pytz


# creating timezone aware date 

dt = datetime(2025,10,25,7,18,30,7800,tzinfo=pytz.UTC)
# print(dt)

dt_now = datetime.now(tz=pytz.UTC)
# print(dt_now)

# datetime — the built-in Python class for working with dates and times.

# pytz — an external library used to manage timezones (like UTC, Asia/Kolkata, etc.).

# 🧠 By default, datetime objects in Python are naive, meaning they don’t contain timezone information.
# pytz helps you make them aware — timezone-aware datetime objects.

# 🔧 Bonus: Example of Converting Between Timezones


utc_time = datetime.now(pytz.UTC)
# print("UTC Time:", utc_time)

india_tz = pytz.timezone("Asia/Kolkata")
india_time = utc_time.astimezone(india_tz)
# print("India Time:", india_time)

us_time = utc_time.astimezone(pytz.timezone("US/Mountain"))
# print("US Time: ",us_time)


# To print out all time zones in pytz
# for tz in pytz.all_timezones:
#     print(tz)


# convert localize time to another timezone

dt_mtn = datetime.now()
asia_timezone = pytz.timezone("Asia/Kolkata")
localize_time = asia_timezone.localize(dt_mtn)
print('Indian Time',localize_time)

us_central = localize_time.astimezone(pytz.timezone("US/Central"))
print("US Central Time",us_central)

# strftime -> used to date to str
# convert str to date
dt_str = 'November 11, 2025'
dt2 = datetime.strptime(dt_str,'%B %d, %Y')
print(dt2)