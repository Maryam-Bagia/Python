info = {
    "name" : "Maryam Bagia",
    "age" : 16,
    "type" : "student"                 # A simple dictionary.
}


#info.keys()

keys = info.keys()
print(keys)


# info.values()

values = info.values()                             
print(values)


# info.items()

items = info.items()               
print(items)


# info.get("key")

age = info.get("age")
print("age = ",age)


# info.update({new_dict})

info.update({"branch" : "Computer Science","Profession" : "Data Scientist"})
print(info)