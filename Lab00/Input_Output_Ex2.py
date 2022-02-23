print("Enter number you need to include into the float list:")
elements = int(input())
numbers = []

for i in range(0, elements):
    print("Enter number at location", i, ":")
    item = float(input())
    numbers.append(item)

print("User List:", numbers)