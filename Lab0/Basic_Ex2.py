print("Printing current and previous number and their sum in a range(100)")
previous_num = 0

for i in range(1, 101):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
    previous_num = i