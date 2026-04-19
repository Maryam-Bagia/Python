# Activity - 6

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("Enter the number of terms: "))

print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i),end=" ")

# Output:
# Enter the number of terms: 10
# Fibonacci sequence:
# 0 1 1 2 3 5 8 13 21 34



