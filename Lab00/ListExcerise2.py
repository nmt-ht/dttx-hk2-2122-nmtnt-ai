list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

print("List 1:", list1)
print("List 2:", list1)
print("Iterate both lists simultaneously")

for x, y in zip(list1, list2[::-1]):
    print(x, y)