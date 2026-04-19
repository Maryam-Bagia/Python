# Program to find GCD of two numbers

# Step 1: Take two numbers as input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Step 2: Euclidean algorithm using while loop
while num2 != 0:   # Repeat until num2 becomes 0
    remainder = num1 % num2
    num1 = num2
    num2 = remainder

# Step 3: At the end, num1 will hold the GCD
print("GCD is:", num1)
