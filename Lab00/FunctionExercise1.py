def subtraction(a, b):
    return a - b

def addition(a, b):
    return a + b

print("Please input number 1:")
a = int(input())
print("Please input number 2:")
b = int(input())

additionStr = "Addition {0} and {1} is: {2} "
print(additionStr.format(a, b, addition(a, b)))
print("Subtraction {0} and {1} is: ".format(a, b), subtraction(a, b))
