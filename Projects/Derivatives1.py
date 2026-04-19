import sympy as sp


# Taking input from the user

expr = input("Enter a function to differentiate (e.g., x**2 + 3*x + 5): ")
var = input("Enter the variable with respect to which you want to differentiate (e.g., x): ")


# Converting the input into a symbolic expression

x = sp.symbols(var)
function = sp.sympify(expr)


# Finding the derivative

derivative = sp.diff(function, x)


# Printing the result
print(f"The derivative of {expr} with respect to {var} is: {derivative}")
