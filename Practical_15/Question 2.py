# Activity - 2

from Practical_15 import arithmetic

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print(f"The sum of {a} and {b} is: {arithmetic.add(a, b)}")
print(f"The difference of {a} and {b} is: {arithmetic.subtract(a, b)}")
print(f"The product of {a} and {b} is: {arithmetic.multiply(a, b)}")
print(f"The division of {a} by {b} is: {arithmetic.divide(a,b)}")

# Output:
# Enter the first number: 10
# Enter the second number: 5
# The sum of 10.0 and 5.0 is: 15.0
# The difference of 10.0 and 5.0 is: 5.0
# The product of 10.0 and 5.0 is: 50.0
# The division of 10.0 by 5.0 is: 2.0


