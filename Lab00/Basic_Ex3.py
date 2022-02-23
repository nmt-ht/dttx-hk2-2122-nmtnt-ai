# Create a new list from a two list using the following condition
# Given a two list of numbers, write a program to create a new list such that the new list 
# should contain odd numbers from the first list and even numbers from the second list.

def merge_list(list1, list2):
    result_list = []
    
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
    
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("list 1: ", list1, "\n")
print("list 2: ", list2, "\n")
print("merge list:", merge_list(list1, list2))