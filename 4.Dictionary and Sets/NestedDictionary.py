# We can create nested dictionaries in python.

student = {
    "name" : "Maryam Bagia",                            # Main dictionary.
    "sem" : 2,
    "subjects" : {
        "Python" : 29,
        "Maths" : 28,                                   # Sub dictionary.
        "Chemistry" : 29,
    },
    "SPI" : 9.00
}

# Accessing whole dictionary.

print(student)


# Accessing only sub dictionary.

print(student["subjects"])


# Accessing only any element from sub dictionary.

print(student["subjects"]["Python"])
