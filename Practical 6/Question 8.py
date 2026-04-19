# Activity-8:

import math

a = float(input("Enter coefficient a : "))
b = float(input("Enter coefficient b : "))
c = float(input("Enter coefficient c : "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / 2*a
    root2 = (-b - math.sqrt(discriminant)) / 2*a
    print(f"The roots are {root1} and {root2}")
elif discriminant == 0:
    root = -b / 2*a
    print(f"The root is {root}")
else:
    print("The equation has no real roots.")

# Output:
# Enter coefficient a : 1
# Enter coefficient b : -3
# Enter coefficient c : 2
# The roots are 2.0 and 1.0

