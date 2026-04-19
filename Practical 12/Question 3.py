# Activity - 3

dict1 = {'a': 1, 'b': 2, 'c': 3}

# Adding an item
dict1['d'] = 4

# Updating an item
dict1['b'] = 5

# Removing an item
dict1.pop('a')

# Getting a value for a key
value = dict1.get('c')

# Checking if a key exists
key_exists = 'd' in dict1

# Clearing all items
dict1.clear()

print("Updated Dictionary:", dict1)
print("Value of 'c':", value)
print("Does 'd' exist?",key_exists)

# Output:
# Updated Dictionary: {}
# Value of 'c': 3
# Does 'd' exist? True


