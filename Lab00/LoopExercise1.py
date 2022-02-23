# Print list in reverse order using a loop

init_lst = [10, 20, 30, 40, 50]
print("Current list: ", init_lst)
# reverse list
reversed_list = reversed(init_lst)
result = []
# iterate reversed list
for item in reversed_list:
    result.append(item)

print("Reversed list: ", result)