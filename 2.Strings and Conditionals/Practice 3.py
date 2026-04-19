# Write a program to check if a given number by user is even or odd.

num = int(input("Enter a number:"))

if((num % 2) == 0):
    print("This is an even number.")
elif(num < 0):
    print("This is neither even nor odd number.")
else:
    print("This is an odd number.")        