from datetime import datetime, timedelta

given_date = datetime(2022, 1, 10)
print("Given date")
print(given_date)

days_to_subtract = 7
res_date = given_date - timedelta(days=days_to_subtract)
print("New Date after subtracting of 7")
print(res_date)