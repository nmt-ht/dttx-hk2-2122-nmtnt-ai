import datetime
from time import gmtime, strftime

print("GMT:", strftime("%Y-%m-%d %H:%M:%S", gmtime()))

# Print date and time
print("Current date time is: ", datetime.datetime.now())

# only time
print("Current time only is: ", datetime.datetime.now().time())