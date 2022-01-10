from datetime import datetime
from time import process_time_ns

given_date = datetime(2022, 1, 1)
print("Given date: ", given_date)

print("Find the day of the week of a given date")
# to get weekday as integer
print(given_date.today().weekday())

# To get the english name of the weekday
print("This day is", given_date.strftime('%A'))