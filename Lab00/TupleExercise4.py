def check(t):
    return all(i == t[0] for i in t)

tuple1 = (1, 1, 1, 1)
print(tuple1)
tuple2 = (1, 2, 4, 1)
print(tuple2)
print("Tuple 1 is the same: ", check(tuple1))
print("Tuple 2 is the same: ", check(tuple2))