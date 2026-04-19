# WAP to search for a number x in this tuple using loop.
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 16
idx = 0

for num in tup:
    if(num == x):
        print("Found at index :",idx)
    idx = idx + 1    