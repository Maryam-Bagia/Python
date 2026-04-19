# Activity - 1

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial of", num, "is",factorial(num))

# Output:
# Enter a number: 5
# Factorial of 5 is 120


