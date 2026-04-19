# Program to find LCM of two numbers

# Step 1: Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Store original values (because we will modify num1, num2 in GCD calculation)
a = num1
b = num2

# Step 2: Find GCD using Euclidean algorithm
while num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder

gcd = num1   # GCD is stored in num1 now

# Step 3: Find LCM using formula (a*b) // GCD
lcm = (a * b) // gcd

# Step 4: Print result
print("LCM is:", lcm)
