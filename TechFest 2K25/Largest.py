# Program to find the largest element in an array with user input

# taking input
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

# assume first element is largest
largest = arr[0]

# loop through array
for num in arr:
    if num > largest:
        largest = num

print("The largest element in the array is:", largest)




