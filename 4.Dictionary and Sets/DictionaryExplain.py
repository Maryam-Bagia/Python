# Dictionaries in python are used to store data values in "key:value" pairs.
# They are unordered mutable and dont allow duplicate keys.

info = {
    "name" : "Maryam Bagia",
    "age" : 16,
    "type" : "student"                 # A simple dictionary.
}

print(info)
print(type(info))



# Accessing dict elements individually.

print(info["name"])
print(info["age"])
print(info["type"])