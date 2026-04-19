# Activity-8:

lst = [10, 5, 8, 3, 7]

lst.append(12)  
lst.remove(8)
print("List:", lst, "Length:", len(lst), "Index 2:", lst[2]) 

lst.sort() 
print("Sorted:", lst) 

lst.reverse() 
print("Reversed:",lst)

# Output:
# List: [10, 5, 3, 7, 12] Length: 5 Index 2: 3
# Sorted: [3, 5, 7, 10, 12]
# Reversed: [12, 10, 7, 5, 3]


