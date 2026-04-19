# Activity-3:

import math

print("1.Circle")
print("2.Rectangle")
print("3.Triangle")

shape = input("Enter shape in lowercase :")

if(shape == "circle"):
    r = float(input("Enter radius of circle : "))
    area = math.pi*r**2
    print(f"Area of given circle = {area:.2f}")
elif(shape == "rectangle"):
    l = float(input("Enter length of rectangle : "))
    b = float(input("Enter breadth of rectangle : "))
    area = l*b
    print(f"Area of given rectangle = {area:.2f}")
else:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"Area of the triangle = {area:.2f}")

# Output:
# Enter shape in lowercase :circle
# Enter radius of circle :5
# Area of given circle = 78.54



