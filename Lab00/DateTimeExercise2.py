from datetime import datetime

date_string = "Feb 25 2020  4:20PM"
print("Date Time string: ", date_string)
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print("Convert string into a datetime object: ", datetime_object)