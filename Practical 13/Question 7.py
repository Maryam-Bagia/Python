# Activity - 7

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("GCD of", num1, "and", num2, "is", gcd(num1,num2))

# Output:
# Enter the first number: 56
# Enter the second number: 98
# GCD of 56 and 98 is 14


