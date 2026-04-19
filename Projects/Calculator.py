# Simple calculator.

print("Hello!\nWelcome to my simple calculator.")

print("(1) Addition (+) :")
print("(2) Subtraction (-) :")
print("(3) Multiplication (*) :")
print("(4) Division (/) :")
print("(5) Modulus (%) :")


a = float(input("Enter first number :"))
b = float(input("Enter second number :"))

opt = input("Select operation symbol :")

if(opt == "+"):
    print(f"Addition of {a} and {b} is = {a+b}")
elif(opt == "-"):
    print(f"Subtraction of {a} and {b} is = {a-b}")
elif(opt == "*"):
    print(f"Multiplication of {a} and {b} is = {a*b}")
elif(opt == "/"):
    print(f"Division of {a} and {b} is = {a/b}")
elif(opt == "%"):
    print(f"Modulo of {a} and {b} is = {a%b}")
else:
    print("error. enter valid inputs.")

print("Thank you for using it.")
print("                                                         Presented by - Maryam Bagia")
