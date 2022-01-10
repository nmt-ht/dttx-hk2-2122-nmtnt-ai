list1 = [5, 10, 15, 20, 25, 50, 20]
print("Original list: ", list1)
# get the first occurrence index
index = list1.index(25)
print("Index is: ", index, " value is: ", list1[index], "and replace the new value is 'tunguyen'")
# update item present at location
list1[index] = "tunguyen"
print(list1)