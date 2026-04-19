# Activity - 5

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# 1. Concatenating tuples
new_tuple = my_tuple + (6, 7)
print("Concatenated tuple:", new_tuple)

# 2. Repeating tuple
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)

# 3. Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# 4. Slicing the tuple
print("Sliced tuple (2 to 4):", my_tuple[1:4])

# 5. Checking if an element exists
print("Is 3 in the tuple?", 3 in my_tuple)
print("Is 6 in the tuple?", 6 in my_tuple)

# 6. Finding the index of an element
print("Index of 4:", my_tuple.index(4))

# 7. Counting occurrences of an element
print("Count of 3:", my_tuple.count(3))

# 8. Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed tuple:",mixed_tuple)

# Output:
# Concatenated tuple: (1, 2, 3, 4, 5, 6, 7)
# Repeated tuple: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
# First element: 1
# Last element: 5
# Sliced tuple (2 to 4): (2, 3, 4)
# Is 3 in the tuple? True
# Is 6 in the tuple? False
# Index of 4: 3
# Count of 3: 1
# Mixed tuple: (1, 'Hello', 3.14, True)

