str1 = "Welcome to VietNam. Vietnam has a lot of beautiful view. vietname awesome, isn't it?."
sub_string = "VietNam"

# convert string to lowercase
temp_str = str1.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("Statemment is '{0}'".format(str1))
print("The VietNam count is:", count)