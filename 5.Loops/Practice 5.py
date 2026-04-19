# Search for a number X in the following tuple using loop.
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
i = 0

while(i<len(tup)):
    if(tup[i] == x):
        print("FOUND at index :",i)
    else:
        print("Finding.....")    
    i = i + 1    