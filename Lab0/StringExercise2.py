print("Arrange string characters such that lowercase letters should come first")

str1 = "TuNGuyen"
print('Original String:', str1)

lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list
        lower.append(char)
    else:
        # add uppercase characters to lower list
        upper.append(char)

# Join both list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)