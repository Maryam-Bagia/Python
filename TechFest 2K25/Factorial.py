num = int(input("Enter a number to find it's factorial:"))

fact = 1

for i in range(num,0,-1):
    fact =fact * i

print(f"The factorial of {num} is {fact}")