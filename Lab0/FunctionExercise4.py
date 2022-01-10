# Create a function with variable length of arguments
def func1(*args):
    for i in args:
        print(i)

print("Create a function with variable length of arguments")
print("Call func 1 with 3 args: 20, 40, 60")
func1(20, 40, 60)
print("Call func 2 with 3 args: 80, 100")
func1(80, 100)