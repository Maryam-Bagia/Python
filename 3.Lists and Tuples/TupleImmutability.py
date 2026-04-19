tup = (2, 1, 4, 3)

# Printing whole tuple.

print(tup)


# Accessing all elements individually.

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])


# Assigning or modifying any element which is not allowed in tuple as they are immutable. this will give error.

mod = tup[1] = 5
print(mod)